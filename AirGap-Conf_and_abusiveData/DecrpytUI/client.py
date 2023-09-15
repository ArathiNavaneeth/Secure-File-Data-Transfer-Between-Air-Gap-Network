import socket
import os

while True:
	try:
		s=socket.socket()
		host="DESKTOP-F4JBRL3"
		port = 8081
		s.connect((host,port))

		filename="okay.txt"
		
		fdata=s.recv(1024).decode()
		print(fdata,type(fdata))
		print("File Recieved..")
	except Exception as e:
		print(e)