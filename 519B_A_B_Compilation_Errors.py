n = int(raw_input())

string1_list_int = map(int, raw_input().split())
string2_list_int = map(int, raw_input().split())
string3_list_int = map(int, raw_input().split())

a,b,c = sum(string1_list_int), sum(string2_list_int), sum(string3_list_int)

print a - b
print b - c