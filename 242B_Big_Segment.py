n = int(raw_input())
minimum,maximum = float('inf'), 0

for x in range(0, n) :

	l, r = map(int, raw_input().split())

	if l <= minimum and r >= maximum :

		k = x + 1
		minimum = l
		maximum = r

	elif l < minimum :

		k = 0
		minimum = l

	elif r > maximum :

		k = 0
		maximum = r

if k > 0 :

	print k

else :

	print '-1'