import socket

data_store = {}

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
          response = handle_command(data.decode())
          connection.sendall(response + b'\n')
        else:
          break
    finally:
      connection.close()

def handle_command(command):
  parts = command.split()
  cmd = parts[0].upper()

  if cmd == 'SET' and len(parts) == 3:
    key, value = parts[1], parts[2]
    data_store[key] = value
    return b'OK'

  elif cmd == 'GET' and len(parts) == 2:
    key = parts[1]
    return data_store.get(key, b'(nil)').encode()

  elif cmd == 'DEL' and len(parts) == 2:
    key = parts[1]
    if key in data_store:
      del data_store[key]
      return b'OK'
    else:
      return b'(nil)'

  else:
    return b'Error: Unsupported command'

if __name__ == '__main__':
  start_server()