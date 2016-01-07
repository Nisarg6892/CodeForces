# import re

string = raw_input()
a = raw_input()
b = raw_input()
string_backward = string[::-1]

# one = string.index(a)

one_forward = string.find(a)
one_backward = string_backward.find(a)

two_forward = string[one_forward+len(a):].find(b)
two_backward = string_backward[one_backward+len(a):].find(b)

if one_forward != -1 and two_forward != -1 and one_backward != -1 and two_backward != -1 :

	print 'both'

elif one_forward != -1 and two_forward != -1 :

	print 'forward'

elif one_backward != -1 and two_backward != -1 :

	print 'backward'

else :

	print 'fantasy'