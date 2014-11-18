__author__ = 'cbilbrey.py@gmail.com'

# rcw55
# kevinrmeyey
# erinbailey

from lock_system import *

class CubbyDB():
	def __init__(self):
		self.cubbies = {}

	def add(self, cubby):
		self.cubbies[cubby.ID] = cubby

	def __str__(self):
		print_str = ''
		for i in self.cubbies:
			print_str = print_str + '%d ' % self.cubbies[i].value
		return print_str

	def readSum(self):
		theSum = 0
		for i in self.cubbies:
			theSum = theSum + self.cubbies[i].value
		return theSum

class Cubby():
	def __init__(self, value, ID):
		self.value = value
		self.ID = ID

	def __str__(self):
		return str(self.value)

	def add(self, num):
		self.value = self.value + num

	def sub(self, num):
		self.value = self.value - num

a = CubbyDB()
b = Cubby(3, 12)
c = Cubby(4, 13)
d = Cubby(5, 14)
e = Cubby(6, 15)
a.add(b)
a.add(c)
a.add(d)
a.add(e)
print(a.readSum())