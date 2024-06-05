from time import time

from pieraknet.packets.frame_set import Frame, FrameSet
from pieraknet.protocol_info import ProtocolInfo
from pieraknet.packets.acknowledgement import Ack, Nack
from pieraknet.handlers.connection_request import ConnectionRequestHandler
from pieraknet.handlers.online_ping import OnlinePingHandler
from pieraknet.packets.online_ping import OnlinePing
from pieraknet.packets.new_incoming_connection import NewIncomingConnection
from pieraknet.packets.disconnect import Disconnect
from pieraknet.buffer import Buffer

class Connection:
    def __init__(self, address, server, mtu_size, guid):
        self.address = address
        self.mtu_size = mtu_size
        self.server = server
        self.guid = guid
        self.connected = False
        self.recovery_queue = {}
        self.ack_queue = []
        self.nack_queue = []
        self.fragmented_packets = {}
        self.compound_id = 0
        self.client_sequence_numbers = []
        self.client_sequence_number = 0
        self.server_sequence_number = 0
        self.queue = FrameSet()
        self.server_reliable_frame_index = 0
        self.client_reliable_frame_index = 0
        self.channel_index = [0] * 32
        self.last_receive_time = time()

    def update(self):
        if (time() - self.last_receive_time) >= self.server.timeout:
            self.disconnect()
        self.send_ack_queue()
        self.send_nack_queue()
        self.send_queue()

    def send_data(self, data: bytes):
        self.server.send(data, self.address)

    def handle(self, data):
        self.last_receive_time = time()
        self.server.logger.info(f"New Packet: {data}")
        packet_type = data[0]
        if packet_type == ProtocolInfo.ACK:
            self.handle_ack(data)
        elif packet_type == ProtocolInfo.NACK:
            self.handle_nack(data)
        elif ProtocolInfo.FRAME_SET_0 <= packet_type <= ProtocolInfo.FRAME_SET_F:
            self.handle_frame_set(data)
            self.server.logger.info("Frame Set handled.")  # Log that the frame set was handled

    def handle_ack(self, data: bytes):
        self.server.logger.info("Handling ACK packet...")
        packet = Ack(data)
        packet.decode()
        for sequence_number in packet.sequence_numbers:
            self.recovery_queue.pop(sequence_number, None)

    def handle_nack(self, data: bytes):
        self.server.logger.info("Handling NACK packet...")
        packet = Nack(data)
        packet.decode()
        for sequence_number in packet.sequence_numbers:
            if sequence_number in self.recovery_queue:
                lost_packet = self.recovery_queue[sequence_number]
                lost_packet.sequence_number = self.server_sequence_number
                self.server_sequence_number += 1
                lost_packet.encode()
                self.send_data(lost_packet.data)
                del self.recovery_queue[sequence_number]

    def handle_frame_set(self, data):
        self.server.logger.info("Handling Frame Set...")
        buf = Buffer(data)
        frame_set = FrameSet()
        frame_set.decode(data)
        if frame_set.sequence_number not in self.client_sequence_numbers:
            self.client_sequence_numbers.append(frame_set.sequence_number)
            self.ack_queue.append(frame_set.sequence_number)
            hole_size = frame_set.sequence_number - self.client_sequence_number
            if hole_size > 0:
                self.nack_queue.extend(
                    range(self.client_sequence_number + 1, hole_size))
            self.client_sequence_number = frame_set.sequence_number
            for frame in frame_set.frames:
                if not (2 <= frame.reliability <= 7 and frame.reliability != 5):
                    self.handle_frame(frame)
                else:
                    hole_size = frame.reliable_frame_index - self.client_reliable_frame_index
                    if hole_size == 0:
                        self.handle_frame(frame)
                        self.client_reliable_frame_index += 1

    def handle_fragmented_frame(self, packet):
        self.server.logger.info("Handling Fragmented Frame...")
        fragments = self.fragmented_packets.setdefault(packet.compound_id, {})
        fragments[packet.index] = packet
        if len(fragments) == packet.compound_size:
            new_frame = Frame()
            new_frame.body = b''.join(fragments[i].body for i in range(packet.compound_size))
            del self.fragmented_packets[packet.compound_id]
            self.handle_frame(new_frame)

    def handle_frame(self, packet):
        self.server.logger.info("Handling Frame...")
        if packet.fragmented:
            self.handle_fragmented_frame(packet)
        else:
            packet_type = packet.body[0]
            if not self.connected:
                if packet_type == ProtocolInfo.CONNECTION_REQUEST:
                    new_frame = Frame(reliability=0)
                    new_frame.body = ConnectionRequestHandler.handle(packet.body, self.server, self)
                    self.add_to_queue(new_frame)
                elif packet_type == ProtocolInfo.NEW_INCOMING_CONNECTION:
                    packet = NewIncomingConnection(packet.body)
                    packet.decode()
                    if packet.server_address[1] == self.server.port:
                        self.connected = True
                        if hasattr(self.server, "interface") and hasattr(self.server.interface, "on_new_incoming"):
                            self.server.interface.on_new_incoming(self)
            else:
                if packet_type == ProtocolInfo.ONLINE_PING:
                    new_frame = Frame(reliability=0)
                    new_frame.body = OnlinePingHandler.handle(OnlinePing(packet.body), self, self.server)
                    self.add_to_queue(new_frame, False)
                elif packet_type == ProtocolInfo.DISCONNECT:
                    self.disconnect()
                elif packet_type == ProtocolInfo.GAME_PACKET:
                    if hasattr(self.server, "interface") and hasattr(self.server.interface, "on_game_packet"):
                        self.server.interface.on_game_packet(packet, self)
                else:
                    if hasattr(self.server, "interface") and hasattr(self.server.interface, "on_unknown_packet"):
                        self.server.interface.on_unknown_packet(packet, self)

    def send_queue(self):
        if not self.queue.frames:
            return

        self.queue.sequence_number = self.server_sequence_number
        self.server_sequence_number += 1
        self.recovery_queue[self.queue.sequence_number] = self.queue
        self.queue.encode()
        self.send_data(self.queue.getvalue())
        self.queue = FrameSet()

    def add_to_queue(self, packet: Frame, is_immediate=True):
        if 2 <= packet.reliability <= 7 and packet.reliability != 5:
            packet.reliable_frame_index = self.server_reliable_frame_index
            self.server_reliable_frame_index += 1
            if packet.reliability == 3:
                packet.ordered_frame_index = self.channel_index[packet.order_channel]
                self.channel_index[packet.order_channel] += 1

        if packet.get_size() > self.mtu_size:
            fragmented_body = [packet.body[i:i + self.mtu_size] for i in range(0, len(packet.body), self.mtu_size)]
            for index, body in enumerate(fragmented_body):
                new_packet = Frame(
                    fragmented=True,
                    reliability=packet.reliability,
                    compound_id=self.compound_id,
                    compound_size=len(fragmented_body),
                    index=index,
                    body=body
                )
                if index != 0:
                    new_packet.reliable_frame_index = self.server_reliable_frame_index
                    self.server_reliable_frame_index += 1
                if new_packet.reliability == 3:
                    new_packet.ordered_frame_index = packet.ordered_frame_index
                    new_packet.order_channel = packet.order_channel
                if is_immediate:
                    self.queue.frames.append(new_packet)
                    self.send_queue()
                else:
                    frame_size = new_packet.get_size()
                    queue_size = self.queue.get_size()
                    if frame_size + queue_size >= self.mtu_size:
                        self.send_queue()
                    self.queue.frames.append(new_packet)
            self.compound_id += 1
        else:
            if is_immediate:
                self.queue.frames.append(packet)
                self.send_queue()
            else:
                frame_size = packet.get_size()
                queue_size = self.queue.get_size()
                if frame_size + queue_size >= self.mtu_size:
                    self.send_queue()
                self.queue.frames.append(packet)

    def send_ack_queue(self):
        if self.ack_queue:
            packet = Ack(sequence_numbers=self.ack_queue)
            packet.encode()
            self.send_data(packet.getvalue())
            self.ack_queue.clear()

    def send_nack_queue(self):
        if self.nack_queue:
            packet = Nack(sequence_numbers=self.nack_queue)
            packet.encode()
            self.send_data(packet.getvalue())
            self.nack_queue.clear()

    def disconnect(self):
        self.server.logger.info("Disconnecting...")
        new_frame = Frame(reliability=0)
        disconnect_packet = Disconnect()
        disconnect_packet.encode()
        new_frame.body = disconnect_packet.getvalue()
        self.add_to_queue(new_frame)
        self.server.remove_connection(self.address)
        if hasattr(self.server.interface, "on_disconnect"):
            self.server.interface.on_disconnect(self)
