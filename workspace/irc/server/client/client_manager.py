import socket as s
import sys

HOST, PORT = 'localhost', 9999
data = ' '.join(sys.argv[1:])

# Create socket
with s.socket(s.AF_INET, s.SOCK_STREAM) as sock:
    # Connect and send data
    s.connect((HOST, PORT))
    s.sendall(bytes(data + '\n', 'utf-8'))

    # Recieve data then shut down
    recieved = str(s.recv(1024), 'utf-8')

print('Sent      {}'.format(data))
print('Recieved: {}'.format(data))