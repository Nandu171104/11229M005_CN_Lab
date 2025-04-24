import re

def is_valid_ipv4(ip):
    pattern = r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'
    if re.match(pattern, ip):
        parts = ip.split('.')
        for part in parts:
            if int(part) < 0 or int(part) > 255:
                return False
        return True
    return False

def get_ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    elif 224 <= first_octet <= 239:
        return 'D (Multicast)'
    elif 240 <= first_octet <= 255:
        return 'E (Reserved)'
    else:
        return 'Invalid'

def is_private_ip(ip):
    parts = list(map(int, ip.split('.')))
    if parts[0] == 10:
        return True
    elif parts[0] == 172 and 16 <= parts[1] <= 31:
        return True
    elif parts[0] == 192 and parts[1] == 168:
        return True
    else:
        return False

# Example Usage
ip_address = input("Enter an IPv4 address: ")

if is_valid_ipv4(ip_address):
    print("✅ Valid IPv4 address.")
    print("Class:", get_ip_class(ip_address))
    print("Private IP:" if is_private_ip(ip_address) else "Public IP.")
else:
    print("❌ Invalid IPv4 address.")

OUTPUT:
 Enter an IPv4 address: 192.168.23.251
✅ Valid IPv4 address.
Class: C
Private IP:
