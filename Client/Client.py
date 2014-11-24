import socket
import time #TODO m: remove once finished
import sys

class Client:
	"""TODO m: Client class description"""
	def __init__(self, host, port):
		self.host = host
		self.port = port

	def run(self):

		try:
			s = socket.socket()
			s.connect((self.host, self.port))
		except Exception, e:
			raise e
			sys.exit()
		
		while True:
			#TODO m: wait for user input
			s.send("Test message")
			sleep(50)

			#TODO m: if input is exit; close connection
			s.close()

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
		session = Client(sys.argv[1], sys.argv[2])
	else:
		print "Missing input arguments"
		print "Please run:"
		print "Client.py [HOSTNAME] [PORT]"
		sys.exit()

	session.run()







		