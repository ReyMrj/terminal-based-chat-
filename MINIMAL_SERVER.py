#server
import socket
import threading

server_address = ("ip address", 6205)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)


server_socket.listen(1)
print("Server is waiting for connections...")

# Function to handle incoming client connections
def handle_client(client_socket):
    while True:
        
        data = client_socket.recv(1024).decode("utf-8")
        print("Received from client:", data)

        # Send a response back to the client
        response = "Server received data" 
        client_socket.send(response.encode("utf-8"))

    # Close the client socket
    client_socket.close()

# Accept incoming client connections
while True:
    client_socket, client_address = server_socket.accept()
    print("Connected to client:", client_address)

    # Start a new thread to handle the client connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
