string_list_int = map(int, raw_input().split())
Set = set(string_list_int)
l = []

for x in Set :

	l.append(string_list_int.count(x))

if len(Set) > 3 or 3 in l :

	print 'Alien'

else :

	if (len(Set) == 2 and 2 in l) or len(Set) == 1 :

		print 'Elephant'

	else :

		print 'Bear'
