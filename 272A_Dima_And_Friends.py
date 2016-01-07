n = int(raw_input())
l = map(int, raw_input().split())

Sum = sum(l)

fingers = []
positions = []
position = 1

for x in range(Sum+1, Sum+6):

	fingers.append(x)

while position <= Sum+5 :

	positions.append(position)
	position = position + (n+1)

print 5-len(set(fingers).intersection(set(positions)))

