d = {}

for x in range(int(raw_input())) :

	s = raw_input()
	n = d.setdefault(s,0)
	d[s] = d[s] + 1

	if n > 0 :

		print s+`n`

	else :

		print 'OK'