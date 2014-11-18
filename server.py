__author__ = 'cbilbrey.py@gmail.com'

from cubby_system import *
from lock_system import *

class Server():
	def __init__(self):
		self.mySock = socket.socket()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        self.host = s.getsockname()[0]
        s.close()
        self.port = int(input('Please enter a port number: '))
        self.mySock.bind((self.host, self.port))
        self.mySock.listen(5)

        while True:
            myConnection, addr = self.mySock.accept()
            data = myConnection.recv(1024)
            if data:
