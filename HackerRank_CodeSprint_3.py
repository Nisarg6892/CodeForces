R = lambda : map(int, raw_input().split())

n, k = R()
boys = R()
girls = R()

boys.sort(Reverse = True)
girls.sort()

count = 0

if boys[0] < girls[-1] :

	for x in range(n) :

		if abs( boys[x] - girls[x] ) <= 10 :

			count = count + 1

		else :

			break

else :

	for x in range(n-1, 1, -1) :

		if abs( boys[x] - girls[x] ) <= 10 :

			count = count + 1

		else :

			break

print count

