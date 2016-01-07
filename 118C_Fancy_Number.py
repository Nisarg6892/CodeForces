n, k = map(int, raw_input().split())
string = raw_input()
d = {}

for x in set(string) :

	count = 0

	for y in list(stirng) :

		if x == y :

			count = count + 1

	d[x] = count

