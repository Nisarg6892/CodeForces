n = int(raw_input())
l = map(int, raw_input().split())
Got = 1

while l[0] != 0 :

	for i in range(0,n) :

		if i % 2 == 0 :

			l[i] = (l[i] + 1)%n

		else :

			if l[i] != 0 :

				l[i] = l[i] - 1				

			else :

				l[i] = n - 1

for x in range(1,n) :

	if l[x] - l[x-1] != 1 :

		Got = 0
		break

if Got == 1 :

	print 'YES'

else :

	print 'NO'