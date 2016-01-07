n = int(raw_input())
string_int = map(int,raw_input().split())

maximum = max(string_int)
index = string_int.index(maximum)
NumberOfSeconds = 0

for x in range(index, 0, -1) :

	string_int[x], string_int[x-1] = string_int[x-1], string_int[x]
	NumberOfSeconds += 1

minimum = min(string_int)

for x in range(len(string_int)-1,0,-1) :

	if string_int[x] == minimum :
	
		index = x
		break

for x in range(index, len(string_int)-1) :

	string_int[x], string_int[x+1] = string_int[x+1], string_int[x]
	NumberOfSeconds += 1

print NumberOfSeconds
