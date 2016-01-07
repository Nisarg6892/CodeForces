l = []

n, m = map(int, raw_input().split())

for x in range(n) :

	string = raw_input()

	for y in string :

		l.append(y)

for x in range(0,n*m) :

	temp = 0

	while m*temp <= n*m :

		temp = temp + 1

		if l[x] == l[x+m*temp] :

			RowNumber = x // m

			for y in range(RowNumber*m, RowNumber*m+m) :

				if y != x :

					if l[x] == l[y] :

						l[x] 


