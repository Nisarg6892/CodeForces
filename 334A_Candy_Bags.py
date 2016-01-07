# n = raw_input()
n = 3
i = 0
j = n ** 2 + 1

for x in range(0, n) :

	i = i + 1
	j = j - 1
	l = []
	l.append(i)
	l.append(j)
	print ' '.join(map(str,l))