n = int(raw_input())
s = raw_input()

l1 = sorted(map(int, list(s[:n])))
l2 = sorted(map(int, list(s[n:])))
# print l1, l2

x = 0
ans = 'YES'

if l1[0] == l2[0] :

	ans = 'NO'
	print ans

else :

	if l1[0] < l2[0] :

		Start = 1

	elif l1[0] > l2[0] :

		Start = 2

	for x in range(1, n) :

		if l1[x] < l2[x] :

			Min = 1

		elif l1[x] > l2[x] :

			Min = 2

		else :

			ans = 'NO'
			print ans
			break

		if Min != Start :

			ans = 'NO'
			print ans
			break

	if ans == 'YES' :

		print ans


