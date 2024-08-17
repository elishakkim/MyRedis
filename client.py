import socket

def run_client():
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  server_address = ('localhost', 6379)
  print(f'Connecting to {server_address[0]}:{server_address[1]}')
  client_socket.connect(server_address)

  try:
    message=b'Hello Server!'
    print(f'Sending: {message}')
    client_socket.sendall(message)

    data = client_socket.recv(1024)
    print(f'Received: {data}')
  finally: 
      print('Closing Connection')
      client_socket.close()

if __name__ == '__main__':
  run_client()