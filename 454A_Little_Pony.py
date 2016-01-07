n = int(raw_input())

for x in range(1, n+1) :

	l = []

	for y in range(1, n+1) :

		divison = n//2+1

		if x > divison :

			x = n - x + 1

		if y > divison-x and y < divison+x :

			l.append('D')

		else :

			l.append('*')

	print ''.join(l)