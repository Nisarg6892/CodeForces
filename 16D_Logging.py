n = int(raw_input())
l = []
count = 1

for x in range(0, n) :

	string = raw_input()

	if string[7] == 'a' :

		if string[1:3] == '12' :

			l.append(0.0 + float(string[4:6])/100.0)

		else :

			l.append(float(string[1:3]) + float(string[4:6])/100.0)

	else :

		if string[1:3] != '12' :

			l.append(float(string[1:3]) + float(string[4:6])/100.0 + 12.0)

		else :

			l.append(float(string[1:3]) + float(string[4:6])/100.0)

for x in range(0, len(l) - 1 ) :

	if l[x] > l[x+1] :

		count = count + 1

# for x in set(l) :

# 	if l.count(x) > 10 :

# 		count = count + l.count(x)/10

for x in range(len(l) - 9) :

	Consecutive = 1
	temp = l[x]


	for y in range(x+1, x+10) :

		if l[y] != temp :

			Consecutive = 0
			break

	if Consecutive == 1 :

		# inside = 0
		count = count + 1
		x = x + 10

print count

