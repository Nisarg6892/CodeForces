n, m = map(int, raw_input().split())
l = map(int, raw_input().split())
d = {}

for x in range(1, n+1) :

	d[x] = d.get(x,'start')

for x in l :

	y = x

	while x <= n :

		if d[x] == 'start' :

			d[x] = str(y)

		x = x + 1

print ' '.join(d.values())