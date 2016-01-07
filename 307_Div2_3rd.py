n, m = map(int, raw_input().split())
BoxesAtPiles = map(int,raw_input().split())

TotalSeconds = 0

# All Students to come at 1st pile
TotalSeconds = TotalSeconds + m 

if n > m :

	# All students reach to individual pile
	TotalSeconds = TotalSeconds + (m-1)

	# delete elements
	while BoxesAtPiles.count(0) != len(BoxesAtPiles) :

		for x in range(0, m) :

			if BoxesAtPiles[x] > 0 : 
				
				BoxesAtPiles[x] = BoxesAtPiles[x] - 1
				TotalSeconds = TotalSeconds + 1


print TotalSeconds

