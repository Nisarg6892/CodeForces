n = int(raw_input())
string = raw_input()

x = string.count('x')
X = string.count('X')

difference = abs(x-X)/2

if difference != 0 :

	if X < x :

		string = string.replace('x','X',difference)

	else :

		string = string.replace('X','x',difference)

print difference,"\n",string
