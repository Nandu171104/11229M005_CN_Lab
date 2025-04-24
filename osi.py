
def physical_layer(data):
    print("Transmitting data as raw bits over physical medium...")
    bits = ''.join(format(ord(c), '08b') for c in data)
    print("Raw bits:", bits)

data = "Hiii"
physical_layer(data)

def data_link_layer(data):
    print("Data Link Layer: Adding checksum for error detection...")
    checksum = sum(ord(c) for c in data) % 256
    print(f"Data: {data} | Checksum: {checksum}")

data = "Hiii"
data_link_layer(data)


import socket

def network_layer():
    print("Network Layer: Fetching IP Address of the local machine...")
    ip_address = "127.0.0.1"  # Using localhost IP
    print(f"Local Machine IP Address: {ip_address}")


import socket

def transport_layer():
    print("Transport Layer: Initiating a TCP connection...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.google.com', 80))
    print("Connected to Google (TCP).")
    s.close()

transport_layer()

def session_layer():
    print("Session Layer: Establishing a session between client and server...")
    session_id = "54321cba"
    print(f"Session ID established: {session_id}")

session_layer()

from cryptography.fernet import Fernet

def presentation_layer(data):
    print("Presentation Layer: Encrypting the data...")
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    print(f"Encrypted Data: {encrypted_data}")

data = "SensitiveData"
presentation_layer(data)

import requests

def application_layer():
    print("Application Layer: Making an HTTP GET request...")
    response = requests.get('https://www.example.com')
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text[:100]}...")

application_layer()

OUTPUT:
Transmitting data as raw bits over physical medium...
Raw bits: 01001000011010010110100101101001
Data Link Layer: Adding checksum for error detection...
Data: Hiii | Checksum: 131
Transport Layer: Initiating a TCP connection...
Connected to Google (TCP).
Session Layer: Establishing a session between client and server...
Session ID established: 54321cba
Presentation Layer: Encrypting the data...
Encrypted Data: b'gAAAAABoCg2AlIFKtJQo2lhPnqHV4Md2NN5CbKQksNa-ZF-xKVSz-4qUL23ofqcsKFXqXEBhoczRkNEpwDNSwvtJFtiRbkktrQ=='
Application Layer: Making an HTTP GET request...
Response Status Code: 200
Response Content: <!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <m...
