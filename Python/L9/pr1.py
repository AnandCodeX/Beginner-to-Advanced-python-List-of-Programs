''' wapp to support =, - and * between Book objects '''

class Book:
	def __init__(self, pages):
		self.pages  = pages
	def __add__(self, other):
		res = self.pages + other.pages
		return res
	def __sub__(self, other):
		res = self.pages - other.pages
		return res
	def __mul__(self, other):
		res = self.pages * other.pages
		return res

b1 = Book(200)
b2 = Book(300)

r1 = b1 + b2;		print(r1)
r2 = b1 - b2;		print(r2)
r3 = b2 * b1;		print(r3)