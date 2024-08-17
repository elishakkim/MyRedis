import socket
import threading 
from myredis.commands import handle_command

def handle_client(connection, client_address):
  print(f'Handling connection from {client_address}')
  try:
    while True: 
      data = connection.recv(1024)
      if data:
        print(f'Received from {client_address}: {data}')
        response = handle_command(data.decode())
        connection.sendall(response + b'\n')
      else:
        break
  finally:
    print(f'Closing connection to {client_address}')
    connection.close()

def start_server():
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  server_address = ('localhost', 6379) 
  print(f'Starting server on {server_address[0]}:{server_address[1]}')
  server_socket.bind(server_address)

  server_socket.listen(5)
  print('Waiting for a connection...')

  while True: 
    connection, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(connection, client_address))
    client_thread.start()

if __name__ == '__main__':
  start_server()