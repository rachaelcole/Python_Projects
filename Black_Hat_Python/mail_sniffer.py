from scapy.all import sniff


def packet_callback(packet): # Define the callback function that will receive each sniffed packet
    print(packet.show())


def main():
    sniff(prn=packet_callback, count=1)  # tells Scapy to start sniffing on all interfaces with no filtering


if __name__ == '__main__':
    main()
