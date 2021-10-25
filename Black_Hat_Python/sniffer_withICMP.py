import ipaddress
import os
import socket
import struct
import sys


class IP:
    def __init__(self, buff=None):
        header = struct.unpack('<BBHHHBBH4s4s', buff)
        self.ver = header[0] >> 4
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
        # Human-friendly IP addresses:
        self.src_address = ipaddress.ip_address(self.src)
        self.dst_address = ipaddress.ip_address(self.dst)
        # Map protocol constants to their names:
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except Exception as e:
            print(f'{e}: No protocol for {self.protocol_num}')
            self.protocol = str(self.protocol_num)


class ICMP:
    def __init__(self, buff):
        header = struct.unpack('<BBHHH', buff)
        self.type = header[0]
        self.code = header[1]
        self.sum = header[2]
        self.id = header[3]
        self.seq = header[4]


def sniff(host):
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((host, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # If we're on Windows, turn on promiscuous mode:
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    try:
        while True:
            # Read a packet
            raw_buffer = sniffer.recvfrom(65535)[0]  # Read in the packet
            # Create an IP header from the first 20 bytes:
            ip_header = IP(raw_buffer[0:20])  # Pass the first 20 bytes to initialise our IP structure
            # If it's ICMP, we want it:
            if ip_header.protocol == 'ICMP':
                print(f'Protocol: {ip_header.protocol} {ip_header.src_address} -> {ip_header.dst_address}')
                print(f'Version: {ip_header.ver}')
                print(f'Header Length: {ip_header.ihl} TTL: {ip_header.ttl}')
                # Calculate where our ICMP header starts:
                offset = ip_header.ihl * 4
                buf = raw_buffer[offset:offset + 8]
                # Create ICMP structure:
                icmp_header = ICMP(buf)
                print(f'ICMP -> Type: {icmp_header.type} Code: {icmp_header.code}\n')
            # Print the detected IP protocol and hosts:
            print(f'Protocol: {ip_header.protocol} {ip_header.src_address} -> {ip_header.dst_address}')
    except KeyboardInterrupt:
        # If we're on Windows, turn off promiscuous mode:
        if os.name == 'nt':
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        sys.exit()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        host = '127.0.0.1'
    sniff(host)
