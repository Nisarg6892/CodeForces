l = []

n = int(raw_input())

for x in range(n) :

	l.append(raw_input())

for x in l :

	if ' rat' in x :

		print x.replace(' rat','')

for x in l :

	if ' woman' in x or ' child' in x :

		if ' woman' in x :

			print x.replace(' woman','')

		else :

			print x.replace(' child','')

for x in l :

	if ' man' in x :

		print x.replace(' man','')


for x in l :

	if ' captain' in x :

		print x.replace(' captain','')

# n = int(raw_input())
# l = [' rat', ' woman_OR_ child', ' man', ' captain']

# for x in range(n) :

# 	string = raw_input()
	

