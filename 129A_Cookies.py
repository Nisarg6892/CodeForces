n = int(raw_input())
l = map(int, raw_input().split())
odd = 0
even = 0

for x in l :

	if x % 2 != 0 :

		odd = odd + 1

	else :

		even = even + 1

if odd % 2 == 0 :

	print n - odd

else :

	print odd