n = int(raw_input())
l = raw_input().split()
Even = 0
Odd = 0
EvenList = []
OddList = []

for x in range(0, n) :

	if int(l[x]) % 2 == 0 :

		Even = Even + 1
		EvenList.append(x)

	else :

		Odd = Odd + 1
		OddList.append(x)

	if ( Even > 1 and Odd == 1 ) :

		print OddList[0] + 1
		break

	elif ( Odd > 1 and Even == 1 ) :

		print EvenList[0] + 1
		break