import socket
import os

while True:
	if len(os.listdir('FileToSend'))>0:
		filename=os.listdir('FileToSend')[0]
		print(filename)


		s=socket.socket()
		host=socket.gethostname()
		print(host)
		port = 8081
		s.bind((host,port))
		s.listen(1)

		print("Waiting For Connection..")
		conn,addr=s.accept()
		print(addr,"Has Beem Connected")

		file=open('FileToSend/'+filename,'r')
		fdata=file.read()
		print(fdata)
		conn.send(fdata)
		file.close()
		print("File Transferred..")
		#os.remove('FileToSend/'+filename)


