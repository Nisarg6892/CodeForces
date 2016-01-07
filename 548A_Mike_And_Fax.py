string = raw_input()
k = int(raw_input())
l = []
index = 0
temp = 1

LengthOfEach = len(string)/k

if len(string) % k == 0 :

	while index < len(string) :

		element = string[index:index+LengthOfEach]
		l.append(element)
		index = index + LengthOfEach

		if element != element[::-1] :

			temp = 0
			break

	if temp == 1 :

		print 'YES'

	else :

		print 'NO'

	# print l

else :

	print 'NO'

