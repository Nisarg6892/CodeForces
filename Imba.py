t = int(raw_input())

for x in range(t) :

	n = int(raw_input())
	
	l = []
	m = []

	final = []

	for y in range(n/2, 0, -1) :

		l.append(y)

	for z in range(n/2+1, n+1) :

		m.append(z)

	i = 0

	while i < len(l) and i < len(m) :

		if n%2 == 0 :
			
			final.append(l[i])
			final.append(m[i])

			i = i + 1

		else :
				
			final.append(m[i])
			final.append(l[i])

			i = i + 1

	if n%2 != 0 :

		final.append(m[-1])

	print ' '.join(map(str,final))