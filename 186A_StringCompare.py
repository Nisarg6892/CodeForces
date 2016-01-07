string1 = raw_input()
string2 = raw_input()

for x in range(0,len(string1)-1):

	for y in range(x+1,len(string1)):

		string1[x], string1[y] = string1[y], string1[x]

print string1, string2