h = raw_input()
a = raw_input()

n = int(raw_input())
l = []
d1 = {}
d2 = {}

final = []
RedList = []

for x in range(0, n) :

	l.append(raw_input().split())
	d1[l[x][1] + l[x][2]] = l[x][0]

	if l[x][3] == 'r' :

		if l[x][1]+l[x][2]+l[x][3] not in RedList :

			final.append(l[x][1]+' '+l[x][2]+' '+l[x][0])

		RedList.append(l[x][1]+l[x][2]+l[x][3])

	else :

		d2[l[x][1] + l[x][2]] = d2.get(l[x][1] + l[x][2],0) + 1

		if d2[l[x][1] + l[x][2]] > 1 :

			if l[x][1]+l[x][2] not in RedList :

				final.append(l[x][1]+' '+l[x][2]+' '+d1[l[x][1]+l[x][2]])

		RedList.append(l[x][1]+l[x][2]+l[x][3])

print final
print RedList

for x in final :

	if 'h' in x :

		print x.replace('h',h)

	else :

		print x.replace('a',a)