n = raw_input()
a, b = raw_input().split()
found = 0

x = int(a)
y = int(b)

for i in range(len(a), len(n)-len(b)+1) :

	if n[i] != '0' :

		# print i

		if int(n[:i]) % x == 0 and int(n[i:]) % y == 0 :

			found = 1
			print 'YES'
			print n[:i]
			print n[i:]
			break

	i = i + 1

if found == 0 :

	print 'NO'