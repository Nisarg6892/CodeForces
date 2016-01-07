n = int(raw_input())
l = []
dictionary = {}

for x in range(0,n) :

	l.append(raw_input())

for x in set(l) :

	dictionary[x] = l.count(x)

print max(dictionary,key=dictionary.get)