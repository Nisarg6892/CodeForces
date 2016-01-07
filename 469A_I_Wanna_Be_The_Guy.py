n = int(raw_input())
GUY = 1

string1_list_int = map(int, raw_input().split())
string2_list_int = map(int, raw_input().split())

if (string1_list_int[0] + string2_list_int[0]) < n :

	print 'Oh, my keyboard!'

else :

	for x in range(1, n+1) :

		if x not in string1_list_int[1:] and x not in string2_list_int[1:] :

			GUY = 0
			break

	if GUY == 1 :

		print 'I become the guy.'

	else :

		print 'Oh, my keyboard!'