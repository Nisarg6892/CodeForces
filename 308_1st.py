n = int(raw_input())
Sum = 0

for x in range(0, n) :

	string_list_int = map(int, raw_input().split())
	Sum = Sum + ( (abs(string_list_int[2] - string_list_int[0]) + 1) * (abs(string_list_int[3] - string_list_int[1]) + 1) )

print Sum