string1 = raw_input()
string2 = raw_input()

l = []

for x in range(0,len(string1)) :

	if string1[x] != string2[x] :

		l.append('1')

	else :

		l.append('0')

print ''.join(l)
