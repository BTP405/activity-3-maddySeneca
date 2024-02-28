import socket
import threading
import pickle

# Function to handle client connections
def handle_client(client_socket, address):
    print(f"Connected: {address}")
    
    # Add client to the list
    clients.append(client_socket)
    
    while True:
        try:
            # Receive pickled message from client
            data = client_socket.recv(1024)
            if not data:
                break
            
            # Unpickle and broadcast message to all clients
            message = pickle.loads(data)
            print(f"Received from {address}: {message}")
            broadcast(message, client_socket)
        except:
            break
    
    # Remove client from the list and close the connection
    clients.remove(client_socket)
    client_socket.close()
    print(f"Disconnected: {address}")

# Function to broadcast message to all clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                # Pickle and send message
                client.send(pickle.dumps(message))
            except:
                # If sending fails, close the connection
                client.close()
                clients.remove(client)

# Main function
def main():
    # Server configuration
    host = '127.0.0.1'
    port = 5555
    
    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    
    print("Server started...")
    
    while True:
        # Accept incoming connections
        client_socket, address = server_socket.accept()
        
        # Create a thread to handle client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

# List to keep track of connected clients
clients = []

if __name__ == "__main__":
    main()
