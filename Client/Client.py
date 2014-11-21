import socket

class Client(Object): # TODO m: Need to pass in Socket I believe...
	"""TODO m: Client class description"""
	def __init__(self, s, message):
		self.s = s
		self.message = messsage

	def run(self):
		"""TODO M: This will be the clients main->
			Read in command line arguments, need to decited on input (maybe YAML file?)
			Handle input/output socket stream? (I just read a networks thing in python so...)
			
			while loop that checks for messages if there is input from client send to other user
			...
		"""
		