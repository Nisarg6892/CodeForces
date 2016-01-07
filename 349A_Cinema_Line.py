n = int(raw_input())
l = map(int, raw_input())
TotalMoney = 0
TwentyFive = 0
Fifty = 0
Hundred = 0
sell = 'YES'

for x in l :

	if x == 25 :

		TwentyFive = TwentyFive + 1

	elif x == 50 :

		Fifty = Fifty + 1

	else :

		Hundred = Hundred + 1

	change = x - 25

	if change > TotalMoney :

		sell = 'NO'
		break

	TotalMoney = TotalMoney + x

	if change > 0 :

		TotalMoney = TotalMoney - change



