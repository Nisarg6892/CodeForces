string = raw_input()
length = len(string)
FindSolution = 0

if string == string[::-1] :

	if length %2 != 0 :

		FindSolution = 1
		print string[:length/2+1] + string[length/2] + string[length/2+1:]

	else :

		FindSolution = 1
		print string[:length/2] + 'a' + string[length/2:]

else :

	for x in range(0,length) :

		if (string[:x]+string[x+1:]) == (string[:x]+string[x+1:])[::-1] :	

			if x <= length/2 :

				FindSolution = 1
				print string[:length-x] + string[x] + string[length-x:]
				break

			else :

				FindSolution = 1
				print string[:length-x-1] + string[x] + string[length-x-1:]
				break

if FindSolution == 0 :

	print 'NA'