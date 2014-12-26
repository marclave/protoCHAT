import socket
import sys
import os
import re
from time import ctime
from threading import Thread

class Server:
	"""TODO m: Description for class name"""
	def __init__(self, host, port):
		self.host = host
		self.port = int(port)
		self.clients = set()

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

			self.clients.add((connection, address))

			print "Got a connection from user @ " + str(address)
			#connection.send("Welcome to the danger zone")

			# Now with this new connection, we open a new thread to deal with that specific client
			# TODO s: Add this connection to a "connection pool", list of all open connections
			newThread = Thread(target = server.talkToClient, args = [connection, address])
			newThread.start()
			#connection.close()

	def talkToClient(self, connection, address):
		while True:
			try:
				#TODO m: need to update this timeout also need to catch better
				connection.settimeout(5)

				data = connection.recv(1024)
				for conn, addr in self.clients:
					#TODO m: change to addr[0] but for now all is local so we need to check port
					if addr[1] != address[1]:
						conn.send('[%s] %s' % (ctime(), data))
					else:
						continue
						#TODO m: Need to update this so that it sends to sender a new line with desired GUI

			except socket.timeout:
				continue
				# Passed timeout	
			except:
				print "Something went wrong"
				break	
		connection.close()		


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
		server = Server(sys.argv[1], sys.argv[2])
	else:
		print "Missing input arguments. Please run:"
		print "		Server.py [HOSTNAME] [PORT] &"
		sys.exit()

	server.run()