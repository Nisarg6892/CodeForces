Count_For_Row = 0

for x in range(0,5) :

	Count_For_Row += 1

	string = raw_input()
	string_int = map(int, string.split())

	Count_For_Column = 0

	for i in string_int :

		Count_For_Column += 1

		if i == 1 :

			RowFinal = Count_For_Row
			ColumnFinal = Count_For_Column
			break

print abs(3 - RowFinal)+abs(3 - ColumnFinal)
