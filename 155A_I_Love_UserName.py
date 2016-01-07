n = int(raw_input())

string_int = map(int,raw_input().split())

AmazingNumber = 0

for x in range(1,len(string_int)) :

	max = string_int[0]
	min = string_int[0]

	for y in range(1, x) :

		if string_int[y] > max :

			max = string_int[y]

		if string_int[y] < min :

			min = string_int[y]

	if string_int[x] > max or string_int[x] < min :

		AmazingNumber += 1

print AmazingNumber
