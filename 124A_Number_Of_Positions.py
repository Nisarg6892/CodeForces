n, a, b = map(int, raw_input().split())
pos1 = []
pos2 = []

for x in range(a, n) :

	pos1.append(x+1)

for x in range(b, -1, -1) :

	pos2.append(n-x)

print len(set(pos1)&set(pos2))