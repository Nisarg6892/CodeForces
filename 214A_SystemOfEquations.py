import math

string_int = map(int,raw_input().split())
n = string_int[0]
m = string_int[1]

c = max(n,m)
SquareRoot = int(math.sqrt(c))

satisfy = 0

for a in range(0, SquareRoot+1):

	for b in range(0, SquareRoot+1):

		if a**2 + b == n and a + b**2 == m :

			# print a,b
			satisfy += 1

print satisfy




