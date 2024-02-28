import socket
import pickle
import threading

# Function to receive messages from server
def receive_messages(client_socket):
    while True:
        try:
            # Receive pickled message from server
            data = client_socket.recv(1024)
            if not data:
                break
            
            # Unpickle and display message
            message = pickle.loads(data)
            print(message)
        except:
            break

# Main function
def main():
    # Server configuration
    host = '127.0.0.1'
    port = 5555
    
    # Connect to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    # Start a thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    
    while True:
        # Send message to server
        message = input()
        client_socket.send(pickle.dumps(message))

# Run the main function
if __name__ == "__main__":
    main()
