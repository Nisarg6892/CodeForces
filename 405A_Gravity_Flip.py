n = int(raw_input())

string_list_int = map(int, raw_input().split())
string_list_int.sort()

print ' '.join(map(str,string_list_int))