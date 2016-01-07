n, k = map(int, raw_input().split())
l = map(int, raw_input().split())
count = 0

# for x in range(0, len(l)-2) :

# 	for y in range(x+1, len(l)-1) :

# 		for z in range(y+1, len(l)) :

# 			if l[y] != l[x]*k :

# 				break

# 			else :

# 				if l[z] == l[y]*k :

# 					count = count + 1

# print count

for x in range(0, n-2) :

	y = l[x]*k
	z = y*k

	# ll = l[:]

	indices = []

	for y1 in range(x+1, n-1) :

		if l[y1] == y :

			# print 'hi'
			indices.append(y1)
		
		# print indices

	for i in indices :

		count = count + l[i+1:].count(z)

print count