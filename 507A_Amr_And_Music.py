n, k = map(int, raw_input().split())
l = map(int, raw_input().split())
m = l[:]
l.sort()
Sum = 0
count = 0
final = []

for x in range(0, len(l)) :

	Sum = Sum + l[x]

	if Sum <= k :

		count = count + 1
		y = m.index(l[x])
		m[y] = ''
		final.append(str(y+1))

	else :

		break

print count

# if len(final) != 0 :
	
print ' '.join(final)
