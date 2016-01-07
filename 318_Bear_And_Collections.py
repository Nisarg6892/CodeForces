# n = int(raw_input())
# l = map(int, raw_input().split())
# count = 0

# while True :

# 	# print 'hello'

# 	Max = max(l)

# 	if l[0] == Max and l.count(Max) == 1 :

# 		print count
# 		break

# 	else :

# 		for x in range(1, n) :

# 			if l[x] == Max :

# 				if l[x] > 0 :
					
# 					l[x] = l[x] - 1

# 				l[0] = l[0] + 1
# 				count = count + 1
# 				# print l

# 				Max = max(l)

# 				if l[0] == Max and l.count(Max) == 1 :

# 					# print 'hi'
# 					# print count
# 					break

d = {1:[2,3], 2:[]}

if 1 in d[2] or 2 in d[1] :

	print 'hi'