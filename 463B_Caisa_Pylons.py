n = int(raw_input())
string_list_int = map(int, raw_input().split())
sum = 0

sum = sum - string_list_int[0]
CoinsNeeded = string_list_int[0]

for x in range(0,len(string_list_int)-1) :

	if string_list_int[x] < string_list_int[x+1] and sum < ( string_list_int[x+1] - string_list_int[x] ) :

		CoinsNeeded = CoinsNeeded + ( string_list_int[x+1] - string_list_int[x] )
		sum = sum + ( string_list_int[x] - string_list_int[x+1] )

	else :

		CoinsNeeded = CoinsNeeded + ( string_list_int[x+1] - string_list_int[x] )
		sum = sum + ( string_list_int[x] - string_list_int[x+1] )

print CoinsNeeded

