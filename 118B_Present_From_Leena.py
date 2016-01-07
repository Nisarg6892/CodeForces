n = int(raw_input())

for x in range(0, 2*n+1) :

	space = ' '*(abs(n-x)*2)

	if x > n :

		x = 2*n - x

	l = []

	for y in range(0, x) :

		l.append(y)

	m = l[::-1]

	l.append(x)

	for y in m :

		l.append(y)

	print space+ ' '.join(map(str, l))