# ARP and RARP simulation using dictionaries

# Simulated network table: IP -> MAC
network_table = {
    "192.168.0.1": "AA:BB:CC:DD:EE:01",
    "192.168.0.2": "AA:BB:CC:DD:EE:02",
    "192.168.0.3": "AA:BB:CC:DD:EE:03"
}

# RARP table: MAC -> IP
rarp_table = {v: k for k, v in network_table.items()}

# Function to simulate ARP
def arp(ip):
    mac = network_table.get(ip)
    if mac:
        print(f"ARP: IP address {ip} is at MAC address {mac}")
    else:
        print(f"ARP: IP address {ip} not found in the network table.")

# Function to simulate RARP
def rarp(mac):
    ip = rarp_table.get(mac.upper())
    if ip:
        print(f"RARP: MAC address {mac} belongs to IP address {ip}")
    else:
        print(f"RARP: MAC address {mac} not found in the network table.")

# Example usage
arp("192.168.0.2")
rarp("AA:BB:CC:DD:EE:03")

OUTPUT:
ARP: IP address 192.168.0.2 is at MAC address AA:BB:CC:DD:EE:02
RARP: MAC address AA:BB:CC:DD:EE:03 belongs to IP address 192.168.0.3
