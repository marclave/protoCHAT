import socket
import time
import sys
import thread

class Client:
	"""TODO m: Client class description"""
	def __init__(self, host, port):
		self.host = host
		self.port = int(port)

	def run(self):

		try:
			s = socket.socket()
			s.connect((self.host, self.port))
		except Exception, e:
			raise e
			sys.exit()

		while True:
			
			#TODO m: Need to poll waiting for stdin so we can recieve messages as they come vs after stdin
			ins = sys.stdin.readline()

			try:
				s.sendall(ins)
			except:
				print 'Send failed'
				sys.exit()
			
			try:
				received = s.recv(1024)
				print received
			except Exception, e:
				print e
				print "Could not recieve"
				sys.exit()

			#TODO m: if input is exit; close connection
			#s.close()	

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