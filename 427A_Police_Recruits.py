n = int(raw_input())
l = raw_input().split()
count = 0
positive = 0

for x in range(0, n) :

	if l[x] == '-1' :

		if positive == 0 :

			count = count + 1

		else :

			positive = positive - 1

	else :

		positive = positive + int(l[x])

print count