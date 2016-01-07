n = int(raw_input())
h = map(int, raw_input().split())
energy = 0
coins = h[0]

for x in range(0, n-1) :

	difference = h[x+1] - h[x]

	if difference >= 0 :

		if energy >= difference :

			energy = energy - difference

		else :

			difference = difference - energy
			energy = 0

			coins = coins + abs(difference)

	else :

		energy = energy + abs(difference)

print coins