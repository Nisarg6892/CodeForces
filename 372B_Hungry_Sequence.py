# n = int(raw_input())
# NumberOfIntegers = 1
# l = [2]
# i = 3

# while NumberOfIntegers < n :

# 	if str(i)[-1] != 5 :

# 		divisible = 0

# 		for x in range(1,len(l)) :

# 			if i % l[x] == 0 :

# 				divisible = 1
# 				break

# 		if divisible == 0 :

# 			l.append(i)

# 			NumberOfIntegers = NumberOfIntegers + 1

# 	i = i + 2

# print ' '.join(map(str,l))

n = int(raw_input())
i = 1000000
l = []

for x in range(0,n) :

	l.append(i)
	i = i + 1

print ' '.join(map(str,l))