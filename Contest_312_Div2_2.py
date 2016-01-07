# n = int(raw_input())
# l = map(int, raw_input().split())
# d = {}
# difference = float('inf')

# # for x in set(l) :

# # 	d[x] = l.count(x)

# for x in l :

# 	d[x] = d.get(x,0) + 1

# # maximum_value = max(d.values())

# w = sorted(d, key = d.__getitem__, reverse = True)
# # print w
# temp = d[w[0]]

# for x in w :

# 	if d[x] == temp :

# 		a = l.index(x)

# 		for z in range(len(l)-1, -1, -1) :

# 			if l[z] == x :

# 				b = z
# 				break

# 		if abs(a-b) < difference :

# 			difference = abs(a-b)
# 			first = a+1
# 			second = b+1

# 	else :

# 		break

# 	temp = d[x]

# print first, second

d = {1:100, 211:213, 3:101, 21:12, 34:213, 400:213}
print max(d, key=d.get)