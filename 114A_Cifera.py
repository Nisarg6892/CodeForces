k = int(raw_input())
l = int(raw_input())
i = 1
result = 0

while k ** i <= l :

	if k ** i == l :

		importance = i - 1
		result = 1
		break

	i = i + 1

if result == 0 :

	print 'NO'

else :

	print 'YES'
	print importance


