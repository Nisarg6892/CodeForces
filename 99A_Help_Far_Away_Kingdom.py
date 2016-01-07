string = raw_input()
# string = '123456789123456789.999'
place = string.find('.')
l = []

# print 'hi'

for x in string :

	if x == '.' :

		break

	else :

		l.append(x)

l_string = ''.join(l)

# print 'hello'
# print l_string

if string[place-1] == '9' :

	print 'GOTO Vasilisa.'

else :

	if int(string[place+1]) >= 5 :

		print int(l_string)+1

	else :

		print int(l_string)

