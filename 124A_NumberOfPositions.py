n, a, b = map(int, raw_input().split())

for x in range(a+1,n+1) :

	if n - x <= b :

		print x
		break