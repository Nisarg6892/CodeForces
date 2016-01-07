def fd():
	print 'd'

class a:

	d = 0
	# q = 55

	# def __init__(self) :

		# self.name = name
		# self.salary = salary
		# d = 54

	def b(self, x,y):
		self.x = x
		self.y = y
		a.d = 1
		fd()

	def c(self, z):
		self.z = z



d = a()
e = a()
print dir(e)
e.c(3)
print a.d
d.b(3,5)
# print a.q
print dir(a)
print dir(d.b)

print d.d
print e.d
print dir(d)
print dir(e)

