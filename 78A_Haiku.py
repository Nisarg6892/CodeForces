string1 = raw_input()
string2 = raw_input()
string3 = raw_input()

string1_count = 0
string2_count = 0
string3_count = 0

for x in string1 :

	if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' :

		string1_count = string1_count + 1

for x in string2 :

	if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' :

		string2_count = string2_count + 1

for x in string3 :

	if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' :

		string3_count = string3_count + 1

if string1_count == 5 and string2_count == 7 and string3_count == 5 :

	print 'YES'

else :

	print 'NO'