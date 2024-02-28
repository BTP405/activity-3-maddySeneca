# Worker Code

import socket
import pickle

def execute_task(conn):
    serialized_task = conn.recv(1024)  # Adjust buffer size as needed
    task = pickle.loads(serialized_task)
    result = task()
    conn.send(str(result).encode())

def start_worker(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', port))  # Bind to the worker's IP and port
    s.listen()
    
    while True:
        conn, addr = s.accept()
        execute_task(conn)
        conn.close()

# Start worker on a specific port
start_worker(5000)  # Choose a port for the worker to listen on