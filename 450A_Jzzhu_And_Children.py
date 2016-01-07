n, m = map(int, raw_input().split())
l = map(int, raw_input().split())
k = []

for x in range(0, n) :

	l[x] = (l[x] + (m-1)) // m

m = max(l)
# k = [i+1 for i,j in enumerate(l) if j == m ]

for x in range(0, n) :

	if l[x] == m :

		k.append(x)

print k[-1]+1