l = map(int, raw_input().split())
s = raw_input()
Sum = 0

for x in s :

	if x == '1' :

		Sum = Sum + l[0]

	if x == '2' :

		Sum = Sum + l[1]

	if x == '3' :

		Sum = Sum + l[2]

	if x == '4' :

		Sum = Sum + l[3]

print Sum