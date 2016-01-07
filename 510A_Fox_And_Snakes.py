n, m = map(int, raw_input().split())

for x in range(1, n+1) :

	if x % 2 != 0 :

		l = []

		for y in range(0, m) :

			l.append('#')

		print ''.join(l)

	elif x % 4 == 0 :

		l = []

		l.append('#')

		for y in range(0, m-1) :

			l.append('.')

		print ''.join(l)

	else :

		l = []

		for y in range(0, m-1) :

			l.append('.')

		l.append('#')

		print ''.join(l)