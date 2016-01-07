n, k = map(int, raw_input().split())
x = (n+1) // 2

if k <= x :

	print 1 + 2*(k-1)

else :

	print 2*(k-x)