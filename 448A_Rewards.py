string_a_int = map(int, raw_input().split())
string_b_int = map(int, raw_input().split())
n = int(raw_input())

SumOfCups = 0
SumOfMedals = 0

ShelfForCups = 0
ShelfForMedals = 0

for x in string_a_int :

	SumOfCups += x

for y in string_b_int :

	SumOfMedals += y

if SumOfCups % 5 == 0 :

	ShelfForCups += SumOfCups / 5

else :

	ShelfForCups += SumOfCups / 5 + 1

if SumOfMedals % 10 == 0 :

	ShelfForMedals += SumOfMedals / 10

else :

	ShelfForMedals += SumOfMedals / 10 + 1

if (ShelfForCups + ShelfForMedals) > n :

	print 'NO'

else :

	print 'YES'