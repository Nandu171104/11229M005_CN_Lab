# chat_server.py
import socket
import threading

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Received: {message}")
            # Broadcast the message to all other clients
            for client in clients:
                if client != client_socket:
                    client.sendall(message.encode())
        except:
            break
    client_socket.close()
    clients.remove(client_socket)

def chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 55547))  # Changed port to 55547
    server_socket.listen()
    print("Server started. Waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected with {addr}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()

if __name__ == '__main__':
    chat_server()


OUTPUT:
Server started. Waiting for connections...
