l=[40,30,3,5,7,8,3,4,5,55,4]

# sorting
x = sorted(l)
print x

def checkPythagorean():

	for a in range(0,len(x)-1):

		for b in range(a+1,len(x)-1):

			for c in range(b+1,len(x)):

				if (x[a]**2 + x[b]**2) == x[c]**2 :

					# print 'hi'
					return 'true'
					break

x = checkPythagorean()
print x