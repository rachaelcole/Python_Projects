import ipaddress
import struct


class IP:
    def __init__(self, buff=None):
        # B = 1-byte unsigned char, H = 2-byte unsigned short, 4S = 4-byte string
        header = struct.unpack('<BBHHHBBH4S4S', buff)
        # Right-shift the byte 4 places, to get the high-order nybble of the byte:
        self.ver = header[0] >> 4
        # Get the second (low-order) nybble of the byte:
        self.ihl = header[0] & 0xF
        self.tos = header[1]
        self.len = header[2]
        self.id = header[3]
        self.offset = header[4]
        self.ttl = header[5]
        self.protocol_num = header[6]
        self.sum = header[7]
        self.src = header[8]
        self.dst = header[9]

        # Human-readable IP addresses
        self.src_address = ipaddress.ip_address(self.src)
        self.dst_address = ipaddress.ip_address(self.dst)

        # Map protocol constants to their names
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}


# To instantiate:
mypacket = IP(buff)
print(f'{mypacket.src_address} -> {mypacket.dst_address}')
