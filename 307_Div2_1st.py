n = int(raw_input())
l = map(int, raw_input().split())
k = [x for x in l]
d = {}
ranking = 1
RepeatCount = 1
answer = []

l.sort(reverse = True)

for x in range(0, len(l)) :


	if x == 0 :

		d[l[x]] = 1

	else :

		if l[x] == l[x-1] :

			RepeatCount = RepeatCount + 1
			d[l[x]] = ranking

		else :

			ranking = ranking + RepeatCount
			d[l[x]] = ranking
			RepeatCount = 1

# print d
# print k
			
for x in k :

	answer.append(d[int(x)])
	# print x

print ' '.join(map(str,answer))