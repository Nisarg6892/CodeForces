R = lambda : map(int, raw_input().split())
n, t = R()
a = R()
Found = 0
Sum = 1

for x in range(0, t) :

	if x + 1 == Sum :

		Sum = (x+1) + a[x]

		if Sum == t :

			Found = 1
			print 'YES'
			break

	# x = Sum

if Found == 0 :

	print 'NO'