data_store = {}

def handle_command(command):
  parts = command.split()
  cmd = parts[0].upper()

  if cmd == 'SET' and len(parts) == 3:
    key, value = parts[1], parts[2]
    data_store[key] = value
    return b'OK'

  elif cmd == 'GET' and len(parts) == 2:
    key = parts[1]
    value = data_store.get(key, None)
    if value is None:
      return b'(nil)'
    else:
      return value.encode()

  elif cmd == 'DEL' and len(parts) == 2:
    key = parts[1]
    if key in data_store:
      del data_store[key]
      return b'OK'
    else:
      return b'(nil)'
    
  elif cmd == 'INCR' and len(parts) == 2:
    key = parts[1]
    value = data_store.get(key, '0')
    try: 
      new_value = int(value) + 1
      data_store[key] = str(new_value)
      return str(new_value).encode()
    except ValueError:
      return b'Error: value is not an integer'
  
  elif cmd == 'DECR' and len(parts) == 2:
    key = parts[1]
    value = data_store.get(key, '0')
    try:
      new_value = int(value) - 1
      data_store[key] = str(new_value)
      return str(new_value).encode()
    except ValueError:
      return b'Error: value is not an integer'

  else:
    return b'Error: Unsupported command'