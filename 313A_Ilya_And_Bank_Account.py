n = raw_input()

if int(n) >= 0 :

	print n

else :

	minimum = min(int(n[-1]), int(n[-2]))
	finalString = n[:len(n)-2]+str(minimum)

	if finalString == '-0' :
		
		finalString = '0'

	print finalString