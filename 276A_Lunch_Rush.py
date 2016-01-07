n, k = map(int, raw_input().split())
Max = float('-inf')

for x in range(0, n) :

	f, t = map(int, raw_input().split())

	if t > k :

		joy = f - t + k

	else :

		joy = f

	if joy > Max :

		Max = joy

print Max