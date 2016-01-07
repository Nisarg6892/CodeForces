n = int(raw_input())
l = []
count = 0

for x in range(0,n) :

	string_list_int = map(int,raw_input().split())
	
	for x in string_list_int :

		l.append(x)

# print l

for x in range(0,len(l),2) :

	for y in range(1,len(l),2) :

		# print x,y

		if l[x] == l[y] :

			count = count + 1

print count