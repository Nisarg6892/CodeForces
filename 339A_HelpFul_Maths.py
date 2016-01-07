string = raw_input()
string_list = list(string)

string_list[:]=(x for x in string_list if x!='+')
string_list_int = map(int,string_list)
# print string_list_int

string_list_int.sort()
string_list_int_string = map(str,string_list_int)
print '+'.join(string_list_int_string)

