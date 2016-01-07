string = raw_input()
string_list = list(string)
l = ['A','H','I','M','O','T','U','V','W','X','Y']
temp = 1

for x in string :

	if x not in l :

		print 'NO'
		temp = 0
		break

if temp == 1 :

	if string_list == string_list[::-1] :

		print 'YES'

	else :

		print 'NO'