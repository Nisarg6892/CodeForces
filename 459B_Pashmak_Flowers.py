n = int(raw_input())
l = []
mul = 1

string_list_int = map(int, raw_input().split())


l.append(string_list_int.count(max(string_list_int)))

if max(string_list_int) != min(string_list_int) :
	
	l.append(string_list_int.count(min(string_list_int)))

# print l

if len(l) != 1 :

	# print 'hi'
	mul = l[0]*l[1]

print str(max(string_list_int)-min(string_list_int))+' '+str(mul)