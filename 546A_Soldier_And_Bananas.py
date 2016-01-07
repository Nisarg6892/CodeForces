k, n, w = map(int, raw_input().split())
Sum = 0

for x in range(1, w+1) :

	Sum = Sum + k*x

if Sum > n :

	print Sum - n

else :

	print '0'