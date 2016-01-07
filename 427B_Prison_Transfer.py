# n, t, c = map(int, raw_input().split())
# l = map(int,raw_input().split())
# count = 0

# for x in range(0,len(l)-c+1) :

# 	# print l[x]	

# 	for y in range(x,x+c) :	

# 		temp = 1	

# 		# print y

# 		if l[y] > t :

# 			temp = 0
# 			break


# 	if temp == 1 :

# 		count = count + 1
# 		# print l[x]

# print count

# R = map(int, raw_input().split())
n, t, c = map(int, raw_input().split())
l = map(int, raw_input().split())
greater = -1
count = 0

for x in range(0, len(l)) :

	if l[x] > t :

		numbers = x - greater - 1
		# print '==='
		# print x, greater, numbers

		if numbers - c + 1 > 0:
			count = count + ( numbers - c + 1 )

		greater = x
if len(l)-greater - c > 0:
	count = count + (len(l)-greater - c)

print count
