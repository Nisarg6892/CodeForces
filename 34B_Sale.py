R = lambda : map(int, raw_input().split())
n, m = R()
l = R()
Sum = 0

l.sort()

for x in range(m) :

	if l[x] < 0 :

		Sum = Sum + l[x]

	else :

		break

print -1*Sum