n = raw_input()
length = len(n)

Sum = 0

for x in range(1, length) :

	Sum = Sum + ( 9 * 10**(x-1) * x )

# print Sum

Sum = Sum + ( (int(n) - (10**(length-1)-1)) * length )

print Sum