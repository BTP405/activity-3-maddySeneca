
import socket
import pickle
import os

def save_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)

def main():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 12345
    BUFFER_SIZE = 4096
    
    save_directory = 'received_files'
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    
    print("Server is listening...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established!")
        
        try:
            data = client_socket.recv(BUFFER_SIZE)
            file_data = pickle.loads(data)
            
            filename = os.path.join(save_directory, file_data['filename'])
            
            save_file(file_data['data'], filename)
            print(f"File saved to {filename}")
            
            client_socket.send("File received successfully!".encode())
        except Exception as e:
            print(f"Error: {e}")
            client_socket.send("Error occurred while receiving the file.".encode())
        finally:
            client_socket.close()

if __name__ == "__main__":
    main()
