a, b, n = map(int, raw_input().split())

def Find_GCD(a, b) :

	if a < b :

		maximum = a

	else :

		maximum = b

	for x in range(maximum, 0, -1) :

		if a % x == 0 and b % x == 0 :

			return x
			break

while True :

	y = Find_GCD(a, n)

	if y <= n :
		
		n = n - y

		if n == 0 :

			print '0'
			break

	z = Find_GCD(b, n)

	if z <= n :
		
		n = n - z

		if n == 0 :

			print '1'
			break