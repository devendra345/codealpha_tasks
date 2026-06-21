from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(IP):
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Protocol: {packet[IP].proto}")
        print("-" * 50)

sniff(prn=packet_callback, count=20)
