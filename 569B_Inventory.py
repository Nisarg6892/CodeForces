n = int(raw_input())
l = map(int, raw_input().split())
m = l[:]
k = [x for x in range(1, n+1)]
final = []

for x in range(0, len(l)) :

	Found = 0

	for y in range(0, x) :

		if l[y] == l[x] :

			Found = 1
			break

	if l[x] < 1 or l[x] > n or Found == 1 :

		for z in range(len(k)) :

			if k[z] not in l :
				
				# print 'hello'
				m[x] = k[z]
				del k[z]
				# print k
				break

	else :

		# final.append(l[x])
		# print 'hi'
		k.remove(l[x])
		# print k

# print ' '.join(map(str, final))
print ' '.join(map(str, m))
# print k
# print l

