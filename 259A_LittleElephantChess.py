NO = 0

for x in range(0,8) :

	string = raw_input()

	if 'BB' in string or 'WW' in string :

		NO = 1

if NO == 1 :

	print 'NO'

else :
	
	print 'YES'