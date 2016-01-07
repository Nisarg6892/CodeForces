n = int(raw_input())
l = map(int, raw_input().split())
i = 0
final = []

for y in range(1, n+1) :

	list_minimum = []

	for x in range(0, n-i) :

		list_minimum.append(min(l[x:x+i+1]))

	final.append(max(list_minimum))

	i = i + 1

print ' '.join(map(str,final))