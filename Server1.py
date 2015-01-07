import socket
import sys
import os
import re
from time import ctime
from threading import Thread

class Server:
	"""TODO m: Description for class"""
	def __init__(self, host, port):
		self.host = host
		self.port = int(port)
		self.clients = set()

	def closeServer(self):
		print "Closing server and disconnecting all clients"
		for connection, address in self.clients:
			# TODO m: Better message and such
			connection.send('[%s] %s' % (ctime(), "Server Closed"))
			connection.close()
		sys.exit()

	def disconnectClient(self, connection, address):
		msg = "Client at " + str(address) + " has Discconnected"
		print msg

		self.clients.remove((connection, address))
		self.sendMessages(connection, address, msg)
		connection.close()

	# Called from the receiveThread each time that there is a message to send to the "chat room"		
	def sendMessages(self, connection, address, data):
		for conn, addr in self.clients:
			try:
				#TODO m: change to addr[0] but for now all is local so we need to check port
				if addr[1] != address[1]:
					conn.send('[%s] %s' % (ctime(), data))
				else:
					continue
					#TODO m: Need to update this so that it sends to sender a new line with desired GUI
			except:
				self.disconnectClient(conn, addr)

	def receiveMessages(self, connection, address):
		while True:
			try:
				data = connection.recv(1024)
				self.sendMessages(connection, address, data)
			except:			
				self.disconnectClient(connection, address)
				break

	def run(self):
		try:
			s = socket.socket()
			s.bind((self.host, self.port))
		except Exception, e:
			raise e
			sys.exit()

		s.listen(5)

		while True:
			try:
				connection, address = s.accept()

				# TODO s: Somehow identify who the client is at this point
				self.clients.add((connection, address))
				print "Got a connection from user @ " + str(address)

				# Now with this new connection, we open a new thread to deal with that specific client
				receiveThread = Thread(target = server.receiveMessages, args = [connection, address])
				receiveThread.start()
			except KeyboardInterrupt:
				self.closeServer()
				

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