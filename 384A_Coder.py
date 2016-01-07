n = int(raw_input())

print ((n+1)//2)**2 + (n//2)**2

for x in range(1, n+1) :

	l = []

	for y in range(1, n+1) :

		if (x+y)%2 == 0 :

			l.append('C')

		else :

			l.append('.')

	print ''.join(l)