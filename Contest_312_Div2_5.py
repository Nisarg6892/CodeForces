# n, q = map(int, raw_input().split())
# s = raw_input()

# for x in range(q) :

# 	t = s

# 	i, j, k = map(int, raw_input().split())
# 	l = []

# 	s = t[:i-1]

# 	if k == 0 :
		
# 		s = s + (''.join(sorted(t[i-1:j]))[::-1])

# 	else :

# 		s = s + ''.join(sorted(t[i-1:j]))

# 	s = s + t[j:]

# print s

l = (1,0,9,3,2,5,11,45,3,33)

if not l :

	print 'empty'

else :

	print 'not empty'

print l

l = (2,4,1,3)

print l
print sorted(l)
print l

if l :

	print 'not empty'

else :

	print 'empty'