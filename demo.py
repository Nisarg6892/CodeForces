b = 23

class a :

	b = 0

	def c(self, p, q) :

		self.p = p
		self.q = q
		self.b = 1
		print a.b

	def d(self, x, y, z) :

		self.x = x
		self.y = y
		self.z = z

print dir(a)

print dir(a.c)

a().c(3,4)

print a().b
# print a().c.b

