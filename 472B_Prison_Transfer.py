n, t, c = map(int, raw_input().split())
l = map(int,raw_input().split())

ans = 1

for x in l :

	if x > t :

		l.remove(x)

y = len(l)

for x in range(0,c) :

	ans = ans * y
	y = y - 1

print ans / 12