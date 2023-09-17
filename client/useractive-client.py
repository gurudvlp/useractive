#!/usr/bin/python

import socket
import subprocess
import time

def get_mousepos():
	position = subprocess.check_output(["xdotool", "getmouselocation"]).decode("utf-8")
	return [int(it.split(":")[1]) for it in position.split()[:2]]
	
def send_packet(host, port):
	print("Sending packet")
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client.sendto(("host active\n").encode(), (host, port))
	client.close()
	
currentPos = get_mousepos()
lastActive = int(time.time())
activeDelay = 3

server_host = "10.4.20.139"
server_port = 2509

while True:
	time.sleep(0.5)
	newPos = get_mousepos()
	
	if not currentPos == newPos:
		if int(time.time()) - lastActive > activeDelay:
			# The mouse has moved, and it has been longer than the inactive
			# timeout period.  That means send a neato packet to the server
			send_packet(server_host, server_port)
		
		lastActive = int(time.time())
		currentPos = newPos
			
		
