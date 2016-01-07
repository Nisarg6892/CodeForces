string1 = raw_input()
string1_int = map(int, string1.split())
n = string1_int[0]
k = string1_int[1]

string2 = raw_input()
string2_int = map(int,string2.split())

count = 0

for x in string2_int:

	if x >= string2_int[k-1] :
		if x != 0 :
			count+=1

	else:
		break

print count