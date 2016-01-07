n, m, a, b = map(int, raw_input().split())

if n % m == 0 :

	print min(a*n,n/m*b)

else :

	temp = n//m
	rate = temp * b

	for x in range(temp*m+1, n+1) :

		rate = rate + a

	print min(a*n, rate, (n/m+1)*b)