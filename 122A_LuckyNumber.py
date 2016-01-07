import re

number = int(raw_input())
lucky = 0

for x in range(4,number+1) :

	searchObj = re.search(r'^[47]*$',str(x))

	if searchObj :

		if number % x == 0 :
			
			lucky = 1
			print 'YES'
			break

if lucky == 0 :

	print 'NO'