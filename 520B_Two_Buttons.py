n, m = map(int, raw_input().split())
L = m // n
l = []
count = 0
count2 = 0

if n >= m :

	print n - m

else :

	temp2 = m/n

	while temp2 >= 2 and temp2 % 2 == 0 :

		# print 'hi'
		temp2 = temp2 / 2
		count2 = count2 + 1

	# print temp2
	if temp2 % 2 == 0 or temp2 == 1 :

		print count2

	else :

		# difference = (m+1) / 2
		l.append( ( L ) + ( n * ((L)+1) - m) )

		if m % 2 == 0 :

			temp = m

			while temp > 0 and temp % 2 == 0 :

				temp = temp / 2
				count = count + 1

				if temp < n :

					break

			if temp < n :

				l.append(n - temp + count)

		# print l
		print min(l)



