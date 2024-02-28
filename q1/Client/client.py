import socket
import pickle

def send_file(server_host, server_port, file_path):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
            filename = file_path.split('/')[-1]
    except FileNotFoundError:
        print("File not found.")
        return
    data = {'filename': filename, 'data': file_data}
    try:
        pickled_data = pickle.dumps(data)
    except pickle.PickleError as e:
        print(f"Pickle error: {e}")
        return
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_host, server_port))
        client_socket.sendall(pickled_data)
        response = client_socket.recv(1024).decode()
        print(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    server_host = '127.0.0.1'  
    server_port = 12345        
    file_path = 'q1/test.txt' 
    send_file(server_host, server_port, file_path)
