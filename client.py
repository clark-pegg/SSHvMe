import socket, signal, os, time, sys

BUFFER_SIZE = 1024

def main(address):
  sock = socket.create_connection((address, 4444))

  pid = os.fork()

  if(pid > 0):
    while True:
      char = sock.recv(1).decode("utf-8")

      if(char == ""):
        os.kill(pid, signal.SIGTERM)
        break

      print(char, end="", flush=True)
  else:
     while True:
      command = input()

      sock.send(command.encode("utf-8") + b"\n")
    
if __name__ == '__main__':
  address = sys.argv[1]

  main(address)