k = int(raw_input())
kString = 1
dict = {}
l = []

s = raw_input()

for x in set(s) :

	if s.count(x) % k != 0 :

		print '-1'
		kString = 0
		break

if kString == 1 :

	for x in set(s) :

		dict[x] = s.count(x) / k

	# print dict

	for key in dict :

		l.append(key * dict[key])

	print ''.join(l) * k

