# n, k = map(int, raw_input().split())
# l = []

# for x in range(0, n) :

# 	i, j = map(int, raw_input().split())
# 	l.append(i+)

# print l

l = [7,20,9,89,34,21,66]
y = l[0]

for x in range(0, len(l)-1) :

	l[x] = l[x+1]

l[x+1] = y

print l