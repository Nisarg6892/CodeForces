l = raw_input().split()
ll = []

for x in set(l) :

	ll.append(l.count(x))

if 6 in ll or ( 2 in ll and 4 in ll ) :

	print 'Elephant'

elif 4 in ll or 5 in ll :

	print 'Bear'

else :

	print 'Alien'