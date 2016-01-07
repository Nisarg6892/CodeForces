n, m, k = map(int, raw_input().split())
string_list_int = map(int, raw_input().split())
count = 0

for x in string_list_int :

	if x == 1 :

		if m > 0 :

			m = m - 1

		else :

			count = count + 1

	else :

		if k > 0 :

			k = k - 1

		elif m > 0 :

			m = m - 1

		else :

			count = count + 1

print count