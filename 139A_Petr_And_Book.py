n = int(raw_input())
day_reading = map(int, raw_input().split())

total = 0
x = 0

while total < n :

	total = total + day_reading[x%7]
	x = x + 1

if x % 7 == 0 :

	print '7'

else :

	print x % 7
