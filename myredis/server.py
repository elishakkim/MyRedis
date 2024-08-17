import socket

def start_server():
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  server_address = ('localhost', 6379) 
  print(f'Starting server on {server_address[0]}:{server_address[1]}')
  server_socket.bind(server_address)


  server_socket.listen(5)
  print('Waiting for a connection...')

  while True: 
    connection, client_address = server_socket.accept()
    try:
      print(f'Connection from {client_address}')
      while True: 
        data = connection.recv(1024)
        if data: 
          print(f'Recieved: {data}')
          connection.sendall(data)
        else:
          break
    finally:
      connection.close()

if __name__ == '__main__':
  start_server()