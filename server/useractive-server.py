#!/usr/bin/python

import socket
import subprocess
import time

listen_port = 2509
listen_host = "0.0.0.0"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((listen_host, listen_port))
print(f"useractive server listening on {listen_host}:{listen_port}")

while True:
	data, client_address = server_socket.recvfrom(1024)
	
	# This is where we would check for special stuff...  like, is this from a
	# specific user?  Does the packet contain special data?  Things like that.
	# For this little PoC, we just make the lights go brrrr
	print(f"useractive received data: {listen_host}:{listen_port}::{client_address}: {data}")
	
	cmd = ["python", "useractive-blinklights.py"]
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = process.communicate()
	
# Even though code can't reach this, we can close out the socket
server_socket.close()
