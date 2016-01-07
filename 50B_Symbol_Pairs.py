s = raw_input()
# s ='nisargshah'
ss = set(s)
ll = list(s)
d = {}
summation = 0

for x in ss :

	count = 0

	for y in ll :

		if x == y :

			count = count + 1

	d[x] = count

for x in d :

	summation = summation + d[x]**2

# print d
print summation
