n, m = map(int, raw_input().split())
l = map(int, raw_input().split())
i = 1
count = 0

for x in range(0, len(l)) :

	if l[x] < i :

		count = count + ( n - (i - l[x]) )
		i = l[x]

	else :

		count = count + (l[x] - i)
		i = l[x]

print count