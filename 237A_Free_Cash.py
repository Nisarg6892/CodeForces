# n = int(raw_input())
# l = []
# count = 1
# final = [1]

# for x in range(0, n) :

# 	string = raw_input()
# 	l.append( string.replace(' ','') )

# # print l

# for x in range(1, len(l)) :

# 	if l[x] == l[x-1] :

# 		count = count + 1

# 	else :

# 		if count > 1 :
			
# 			final.append(count)

# 		count = 1

# final.append(count)
# # print final
# print max(final)

n = int(raw_input())
d = {}

for x in range(0, n) :

	y = raw_input()
	d[y] = d.get(y,0) + 1

print max(d.values())