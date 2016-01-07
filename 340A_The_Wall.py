x, y, a, b = map(int, raw_input().split())
lcm = 0
j = 1
count = 0
started = 0

if x > y :

	greater = x

else :

	greater = y

while True :

	if greater % x == 0 and greater % y == 0 :

		lcm = greater
		break

	greater = greater + 1

# print lcm

if lcm > a and lcm > b :

	print count

else :

	j = a // lcm
	k = b // lcm

	if a % lcm == 0 :

		print k-j+1

	else :

		print k-j

