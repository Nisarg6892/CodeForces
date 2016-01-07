string1 = raw_input()
string2 = raw_input()
string3 = raw_input()
list3 = []

string4 = string1 + string2
list4 = []

for x in string4 :

	list4.append(x)

list4.sort()

for x in string3 :

	list3.append(x)

list3.sort()

if list3 == list4 :

	print 'YES'

else :

	print 'NO'