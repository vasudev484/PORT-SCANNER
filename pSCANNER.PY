#!/bin/python3

import sys
import socket
from datetime import datetime as dt

#Define our target

if (len(sys.argv)) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to ipv4
	
else:
	print("Invalid amount of argument.")
	print("Syntax: python3 pscanner.py <ip>")	
	
# Add a preety banner

print("-" * 50)
print("Scanning Target "+target)
print("Time started: "+str(dt.now()))
print("-" * 50)

try:
	for port in range (40,80):
		s = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) # returns an error indicator
		if result == 0:
			print("Port {} is open".format(port))
			s.close()
		
except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()
