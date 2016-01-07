n = int(raw_input())
l = []
m = []
Sum = 0
d = {}

for x in range(n) :

	string_list_int = map(int, raw_input().split())

	d[string_list_int[0]] = string_list_int[1]

	if string_list_int[0] < 0 :

		l.append(string_list_int[0])

	else :

		m.append(string_list_int[0])

l.sort(reverse = True)
m.sort()

# print l
# print m
# print d

if len(l) > len(m) :

	if len(m) > 0 :

		for x in range(0, len(m)) :

			Sum = Sum + d[m[x]]
			# print Sum

	if len(l) > 0 :

		for y in range(0, len(m)+1) :

			Sum = Sum + d[l[y]]
			# print Sum

	# print 'hi'

elif len(m) > len(l) :

	if len(l) > 0 :

		for x in range(0, len(l)) :

			Sum = Sum + d[l[x]]

	if len(m) > 0 :

		for y in range(0, len(l)+1) :

			Sum = Sum + d[m[y]]

	# print 'hello'

else :

	Sum = Sum + sum(d.values())

	# print 'hey'

print Sum

