t = int(raw_input())

for x in range(0,t) :

	string_int = int(raw_input())

	if 360 % ( 180 - string_int ) == 0 :

		print 'YES'

	else :

		print 'NO'

