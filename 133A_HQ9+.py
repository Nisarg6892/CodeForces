string = raw_input()
Found = 0

for x in string :

	if x == 'H' or x =='Q' or x == '9' :

		Found = 1
		break

if Found == 0 :

	print 'NO'

else :

	print 'YES'