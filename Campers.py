n, k = map(int, raw_input().split())
l = map(int, raw_input().split())

# Full_List = range(1, n+1)
# After_Cut = set(Full_List) - set(l)

# for x in After_Cut :

# 	if (x+1) not in l and (x-1) not in l :

# 		l.append(x)

# print len(l)

l.sort()

Sum = k
# print Sum

Sum = Sum + (l[0] - 1) / 2
# print Sum

for x in range(1, k) :

	difference = l[x] - l[x-1]

	if difference > 3 :

		Sum = Sum + (difference-2)/2

Sum = Sum + (n-l[-1])/2

print Sum