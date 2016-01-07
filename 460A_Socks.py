string = raw_input()
string_int = map(int,string.split())

n = string_int[0]
m = string_int[1]

i = 0

while True:

	i = i + 1

	if i > n :

		print n
		break

	if i % m == 0 :

		n = n + 1

	
