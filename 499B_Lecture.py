n, m = map(int, raw_input().split())
l = []
ans = []

for x in range(0,m) :

	string_list = raw_input().split()

	for y in string_list :
	
		l.append(y)

string_n_list = raw_input().split()

for x in string_n_list :

	if len(l[l.index(x)+1]) < len(l[l.index(x)]) :

		ans.append(l[l.index(x)+1])

	else :

		ans.append(l[l.index(x)])

print ' '.join(ans)