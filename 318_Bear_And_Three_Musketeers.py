import itertools

n, m = map(int, raw_input().split())
d = {}
p = ''
final = []
temp_list = []

for x in range(1, n+1) :

	d[x] = []
	p = p + str(x)

for x in range(m) :

	a, b = map(int, raw_input().split())
	d[a].append(b)

print d

for x in d :

	temp = ''

	temp = temp + str(x)

	for y in d[x] :

		temp = temp + str(y)

	temp_list.append(temp)

print temp_list

l = list(itertools.combinations(p,3))
print l

for x in l :

	# print x[0], x[1], x[2]
	# print d[int(x[1])]

	if ( int(x[0]) in d[int(x[1])] or int(x[1]) in d[int(x[0])] ) and ( int(x[1]) in d[int(x[2])] or int(x[2]) in d[int(x[1])] ) and ( int(x[0]) in d[int(x[2])] or int(x[2]) in d[int(x[0])] ) :

		print x[0], x[1], x[2]

		count = 0

		for y in x :

			for t in temp_list :

				if y in t :

					for every in t :

						if every not in x :

							count = count + 1
							
			# for z in d[int(y)] :

			# 	if str(z) not in x :

		final.append(count)

print final

if len(final) == 0 :

	print '-1'

else :

	print min(final)