n, l = map(int, raw_input().split())
string_list_int = map(int, raw_input().split())
lis = []

string_list_int.sort()
# print string_list_int

if string_list_int[0] != 0 :

	lis.append(string_list_int[0]-0)

for x in range(1,len(string_list_int)) :

	lis.append((string_list_int[x]-string_list_int[x-1])/2.0)

if string_list_int[-1] != l :

	lis.append(l-string_list_int[-1])

# print lis

print '%.10f'%max(lis)