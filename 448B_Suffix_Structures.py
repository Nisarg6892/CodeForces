s = raw_input()
s_list = list(s)
s_list.sort()

t = raw_input()
t_list = list(t)
t_list.sort()

both = 1

if t in s :

	print 'automaton'

for x in t_list :

	if x in s_list :

		s_list.remove()

elif s_list == t_list :

	print 'array'

else :

	for x in t_list :

		if x in s_list :

			s_list.remove(x)

		else :

			both = 0
			print 'need tree'
			break

	if both == 1 :

		print 'both'