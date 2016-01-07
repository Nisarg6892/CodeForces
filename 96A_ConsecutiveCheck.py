s='1001100000001'
temp = ''
count = 1

for x in s:

	if x == temp :

		count = count + 1

		if count == 7 :
			print 'YES'
			break

	temp = x

if count != 7 :

	print 'NO'