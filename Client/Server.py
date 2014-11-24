import socket
import sys
import os

class Server:
	"""TODO m: Description for class name"""
	def __init__(self, host, port):
		self.host = host
		self.port = port

	def run(self):
		
		try:
			s = socket.socket()
			s.bind((self.host, self.port))
		except Exception, e:
			raise e
			sys.exit()

		s.listen(5)

		while True:
			connection, address = s.accept()
			print "Got a connection from" + address
			connection.send("Welcome to the danger zone")
			connection.close

if __name__ == "__main__":

	print "================================="
	print "            protoCHAT            "
	print "          Developed by:          "
	print "		    Marc Laventure          "
	print "             Toasty              "
	print "================================="
	print ""

	if len(sys.argv) > 1:
	#TODO m: check port and host name input?
		server = Server(sys.argv[1], sys.argv[2])
	else:
		print "Missing input arguments. Please run:"
		print "		Server.py [HOSTNAME] [PORT] &"
		sys.exit()

	server.run()


