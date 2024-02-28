# Client Code

import socket
import pickle

def send_task_to_workers(task, workers):
    for worker in workers:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(worker)
            serialized_task = pickle.dumps(task)
            s.send(serialized_task)
            result = s.recv(1024)  # Adjust buffer size as needed
            print(f"Result from {worker}: {result.decode()}")
        except socket.error as e:
            print(f"Error connecting to {worker}: {e}")
        finally:
            s.close()

# Example task to send to workers
def square_number(x):
    return x**2
workers = [('localhost', 5000), ( 'localhost',5000)]  # Update with actual worker IPs and ports
send_task_to_workers(square_number, workers)