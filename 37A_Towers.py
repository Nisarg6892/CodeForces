n = int(raw_input())

string_list_int = map(int,raw_input().split())

s = set(string_list_int)
l = []

for i in s :

	l.append(string_list_int.count(i))

print str(max(l))+' '+str(len(s))