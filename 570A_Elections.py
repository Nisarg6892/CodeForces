n, m = map(int, raw_input().split())
final = []
d = {}
keys = []

for x in range(m) :

	l = map(int, raw_input().split())
	Max = -1

	for y in range(n) :

		if l[y] > Max :

			Max = l[y]
			Candidate = y+1

	final.append(Candidate)

# print final

for x in set(final) :

	d[x] = final.count(x)

# print d

MaximumValue = max(d.values())

for x in d :

	if d[x] == MaximumValue :

		keys.append(x)

# print keys
print min(keys)

# t = {'a':100, 'b':500, 'c':300, 'e':300, 'r':500}

# print list(t, key = t.get)