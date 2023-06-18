#client
import socket
import threading


server_address = ("ip address", 6205)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(server_address)


# Function to handle receiving messages from the server
def receive_messages():
    while True:
        # Receive data from the server
        data = client_socket.recv(1024).decode("utf-8")
        print("Received data from server")


receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()


while True:
    
    message = input("Enter a message ")

    client_socket.send(message.encode("utf-8"))

   

# Close the client socket
client_socket.close()
