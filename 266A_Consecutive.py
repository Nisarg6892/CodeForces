t = int(raw_input())
string = raw_input().lower()
previous = ''
count = 0

for x in string :

	if x == previous :

		count += 1

	previous = x

print count

