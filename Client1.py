import socket
import time
import sys
from threading import Thread

class Client:
	"""TODO m: Client class description"""
	def __init__(self, host, port):
		self.host = host
		self.port = int(port)

	def send(self, connection):
		while True:
			try:
				ins = sys.stdin.readline()
				connection.sendall(ins)
			except:
				print "In client.send, something broke"
				sys.exit()

	def receive(self, connection):
		while True:
			try:
				received = connection.recv(1024)
				print received
			except:
				print "In client.receive, something broke"			
				sys.exit()

	def run(self):
		try:
			s = socket.socket()
			s.connect((self.host, self.port))
		except Exception, e:
			raise e
			sys.exit()
		
		sendData = Thread(target = session.send, args = [s,])
		recieveData = Thread(target = session.receive, args = [s,])
		sendData.start()		
		recieveData.start()

if __name__ == "__main__":

	print "================================="
	print "            protoCHAT            "
	print "          Developed by:          "
	print "         Marc Laventure          "
	print "             Toasty              "
	print "================================="
	print ""

	if len(sys.argv) > 1:
		#TODO m: check port and host name input?
		session = Client(sys.argv[1], sys.argv[2])
	else:
		print "Missing input arguments"
		print "Please run:"
		print "Client.py [HOSTNAME] [PORT]"
		sys.exit()

	session.run()