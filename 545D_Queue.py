n = int(raw_input())
l = map(int, raw_input().split())
l.sort()
Sum = 0
count = 1

for x in range(1, n) :

	Sum = Sum + l[x-1]

	if l[x] >= Sum :

		count = count + 1

	else :

		l[x] = 0

print count