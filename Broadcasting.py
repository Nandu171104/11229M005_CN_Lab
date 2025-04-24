import socket

def broadcast_message(message, broadcast_ip="255.255.255.255", port=9999):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


    sock.sendto(message.encode(), (broadcast_ip, port))
    print(f"Broadcasting message to {broadcast_ip}:{port}")


message = "Hello, this is a broadcast message!"
broadcast_message(message)

Output:
Broadcasting message to 255.255.255.255:9999
