# t = int(raw_input())

for x in range(input()):

	string = raw_input()
	length=len(string)
	
	if length<=10:
		print string
	
	else:
		print string[0]+str(length-2)+string[length-1]


