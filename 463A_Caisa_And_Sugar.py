n, s = map(int, raw_input().split())
l = []

for x in range(0,n) :

	string_list_int = map(int, raw_input().split())

	if s > string_list_int[0] or (s == string_list_int[0] and string_list_int[1] == 0) :

		l.append ( 100 - string_list_int[1] )

if len(l) != 0 :
	
	l = [ x for x in l if x != 100 ]

	if len(l) != 0 :
		
		print max(l)

	else :

		print '0'

else :

	print '-1' 