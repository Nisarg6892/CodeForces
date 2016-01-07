import itertools
Sum = 0

def FindColinear(a, b, c) :

	global Sum

	if d[2*a] != d[2*b] :
		
		z1 = float(d[2*a+1]-d[2*b+1]) / float(d[2*a]-d[2*b])

	elif d[2*a+1] != d[2*b+1] :

		z1 = float(d[2*a]-d[2*b]) / float(d[2*a+1]-d[2*b+1])

	if d[2*b] != d[2*c] :
		
		z2 = float(d[2*b+1]-d[2*c+1]) / float(d[2*b]-d[2*c])

	elif d[2*b+1] != d[2*c+1] :

		z2 = float(d[2*b]-d[2*c]) / float(d[2*b+1]-d[2*c+1])

	if d[2*a] != d[2*c] :

		z3 = float(d[2*a+1]-d[2*c+1]) / float(d[2*a]-d[2*c])

	elif d[2*a+1] != d[2*c+1] :

		z3 = float(d[2*a]-d[2*c]) / float(d[2*a+1]-d[2*c+1])

	if z1 == z2 == z3 :

		Sum = Sum + 1

n = int(raw_input())
m = n
numerator = 1
d = []

for x in range(0,3) :

	numerator = numerator * n
	n = n - 1

numerator = numerator / 6

for x in range(1,m+1) :

	y = map(int, raw_input().split())

	for u in y :

		d.append(u)

l = list(itertools.combinations([x for x in range(0,m)],3))

for x in l :
	
	FindColinear(x[0],x[1],x[2])

print numerator - Sum