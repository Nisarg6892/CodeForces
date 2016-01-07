import re

string = raw_input()

searchObj = re.search(r'.*h.*e.*l.*l.*o.*',string)

if searchObj :

	print 'YES'

else :

	print 'NO'