import socket
import os

# Host to listen on
HOST = '192.168.1.203'  # set this to our own machine's address


def main():
    # Create raw socket, bin to public interface
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    # Create socket object with necessary params for sniffing packets on our network:
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))
    # Include the IP header in the capture:
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)  # Set socket option to include IP headers
    # If using Windows, send an IOCTL to the NIC driver to enable promiscuous mode
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    # Read one packet:
    print(sniffer.recvfrom(65565))  # Prints the entire raw packet with no packet decoding
    # If we are on Windows, turn off promiscuous mode:
    if os.name == 'nt':  # 5
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


if __name__ == '__main__':
    main()
