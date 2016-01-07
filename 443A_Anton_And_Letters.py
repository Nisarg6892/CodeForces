string = raw_input()
s = string[1::3]

if '}' in s :
	
	s = s.replace('}','')

l = []

for x in s :

	l.append(x)

print len(set(l))