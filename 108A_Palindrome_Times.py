a = [0, 1, 2]
l = []
lis = []
s = raw_input()
t = list(s)
t.remove(':')

for x in a :

	for y in range(0,6) :

		if x < 2 or (x == 2 and y <= 3) :

			l = []
			l.append(x)
			l.append(y)
			l.append(y)
			l.append(x)
			string = ''.join(map(str,l))
			lis.append(string)

# print lis
# print 'hello'

for x in lis :

	if int(x) > int(''.join(t)) :

		print x[0:2]+':'+x[2:]
		break

	if int(''.join(t)) >= int(lis[-1]) :

		print '00:00'
		break

