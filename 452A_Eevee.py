n = raw_input()
string = raw_input()
l = []
ll = []

d = { "vaporeon" : "8", "jolteon" : "7", "flareon" : "7", "espeon" : "6", "umbreon" : "7", "leafeon" : "7", "glaceon" : "7", "sylveon" : "7" }

for key, value in d.items() :

	if value == n :

		l.append(key)

if len(l) == 1 :

	print l[0]

else :

	i = 0

	while i < int(n) :

		if string[i] != '.' :

			ll.append(str(i)+string[i])

		i = i + 1

	for x in l :

		GOT = 'yes'

		for y in ll :

			if x[int(y[0])] != y[1] :

				GOT = 'no'
				break

		if GOT == 'yes' :

			print x
			break