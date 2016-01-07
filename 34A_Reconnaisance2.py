n = int(raw_input())
l = map(int, raw_input().split())
q = abs(l[0]-l[1])
z = ''

for x in range(0, len(l)) :

	if x == len(l) - 1 :

		y = 0

	else :

		y = x + 1

	if abs(l[x] - l[y]) < q :

		z = str(x+1)+' '+str(y+1)
		q = abs(l[x] - l[y])

if len(z) != 0 :

	print z

else :

	print '1 2'




