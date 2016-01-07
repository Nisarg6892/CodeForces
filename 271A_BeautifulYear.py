year = raw_input()
year = int(year) + 1
# print year

while True :

	setOfYear = set(str(year))

	if len(setOfYear) == len(str(year)) :

		print year
		break

	else :

		year = int(year) + 1






