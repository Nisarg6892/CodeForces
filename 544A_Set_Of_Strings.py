k = int(raw_input())
string_q = raw_input()

l = []
answer = []

for x in string_q :

	if x not in l :

		l.append(x)

if len(l) < k :

	print 'NO'

else :

	for x in range(k) :

		if x == k-1 :

			answer.append ( string_q[ string_q.index(l[x]) : ] )

		else :

			answer.append ( string_q[ string_q.index(l[x]) : string_q.index(l[x+1]) ] )

	print 'YES'

	for x in answer :

		print x