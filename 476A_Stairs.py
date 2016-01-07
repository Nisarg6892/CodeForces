n, m = map(int, raw_input().split())

if n >= m :
	
	for x in range((n+1)/2, n+1) :

		if x % m == 0 :

			print x
			break

else :

	print '-1'