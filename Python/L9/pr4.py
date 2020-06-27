class Book:
	def __init__(self, nop):
		self.nop = nop
	def __add__(self, other):
		res = self.nop + other.nop
		return Book(res)
	def __str__(self):
		msg = 'nop=' + str(self.nop)
		return  msg


b1 = Book(100)
b2 = Book(200)
b3 = Book(300)

r1 = b1 + b2 + b3;	print(r1)