n = int(raw_input())

first = map(int, raw_input().split())
second = map(int, raw_input().split())
third = map(int, raw_input().split())

minimum = first[0]+second[0]+third[0]

if minimum == n :

	print first[0], second[0], third[0]

else :

	difference = n - minimum
	y = second[0]

	if first[1] - first[0] >= difference :

		x = first[0] + difference

	else :

		x = first[1]
		difference = difference - (first[1]-first[0])

		if second[1] - second[0] >= difference :

			y = second[0] + difference

		else :

			y = second[1]
		
	z = n - x - y

	print x, y, z
