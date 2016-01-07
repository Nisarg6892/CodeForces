n = int(raw_input())
l = []
greater = 0
lower = 0

for x in range(0,n) :

	string_list = map(int,raw_input().split())

	for x in string_list :

		l.append(x)

for x in range(0, len(l), 2) :

	if l[x] > l[x+1] :

		greater = 1
		break

for x in range(0, len(l), 2) :

	if l[x] < l[x+1] :

		lower = 1
		break

if greater == 1 and lower == 1 :

	print 'Happy Alex'

else :

	print 'Poor Alex'

