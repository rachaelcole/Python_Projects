from ctypes import *
import socket
import struct

# Create a IP class that inhertis from ctype module's Structure class
class IP(Structure):
    # Create a _fields_ structure to define each part of the IP header using C types
    _fields_ = [
        # ("name", type, width_in_bits)
        ("ihl", c_ubyte, 4),            # 4-bit unsigned char
        ("version", c_ubyte, 4),        # 4-bit unsigned char
        ("tos", c_ubyte, 8),            # 1-byte char
        ("len", c_ushort, 16),          # 2-byte unsigned short
        ("id", c_ushort, 16),           # 2-byte unsigned short
        ("offset", c_ushort, 16),       # 2-byte unsigned short
        ("ttl", c_ubyte, 8),            # 1-byte char
        ("protocol_num", c_ubyte, 8),   # 1-byte char
        ("sum", c_ushort, 16),          # 2-byte unsigned short
        ("src", c_uint32, 32),          # 4-byte unsigned int
        ("dst", c_uint32, 32)           # 4-byte unsigned int
    ]

    def __new__(cls, socket_buffer=None):
        return cls.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        # Human-readable IP addresses
        self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))
