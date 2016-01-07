NumberOfCoins = int(raw_input())
list_int = map(int, raw_input().split())

list_int.sort(reverse = True)
summation = 0
CoinsNeeded = 0
i = 0

while True :

	CoinsNeeded += 1
	summation += list_int[i]
	i += 1

	if summation > sum(list_int)/2 :

		print CoinsNeeded
		break