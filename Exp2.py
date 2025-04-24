import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Received from {client_address}: {data}")
            client_socket.sendall(data.encode()) 
        except ConnectionResetError:
            print(f"Connection reset by {client_address}")
            break
    client_socket.close()
    print(f"Connection closed with {client_address}")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 55546))
    server_socket.listen(5)
    print("Server started. Listening for connections...")
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == '__main__':
    start_server()


OUTPUT:
Server started. Listening for connections...
