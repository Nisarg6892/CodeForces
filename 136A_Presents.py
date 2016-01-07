n = int(raw_input())

list_int = map(int, raw_input().split())
l = []

for x in range(1,len(list_int)+1) :

	l.append(list_int.index(x)+1)

print ' '.join(map(str,l))