n, m = map(int,raw_input().split())

for x in range(1,n+1) :

	for y in range(1,m+1) :

		if x % 2 != 0 :

			print '#'*

		elif (x % 4 == 0  and y == 1) or (x % 2 == 0 and x % 4 != 0 and y == m ) :

				print '#'

		else :

			print '.'