n, k = map(int, raw_input().split())
string = raw_input()

l = list(string)
s = set(l)
d = {}

Sum = 0
final = 0

for x in s :

	d[x] = l.count(x)

SortedList = d.values()
SortedList.sort(reverse = True)

# print SortedList

for x in SortedList :

	Sum = Sum + x

	if Sum <= k :

		final = final + x**2
		# print final

	else :

		final = final + (k - (Sum - x))**2
		break

print final

