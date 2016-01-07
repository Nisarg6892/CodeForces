t = int(raw_input())

for x in range(0, t) :

	index = []
	count = 0

	n = int(raw_input())
	l = map(int, raw_input().split())

	for y in l :

		z = y%10

		if z in index :

			count = count + 1

		index.append(z)

	print count

