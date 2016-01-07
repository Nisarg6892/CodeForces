string = raw_input()
dictionary = {}
l = []

dictionary[raw_input()] = '0'
dictionary[raw_input()] = '1'
dictionary[raw_input()] = '2'
dictionary[raw_input()] = '3'
dictionary[raw_input()] = '4'
dictionary[raw_input()] = '5'
dictionary[raw_input()] = '6'
dictionary[raw_input()] = '7'
dictionary[raw_input()] = '8'
dictionary[raw_input()] = '9'

# print dictionary

for x in range(0,71,10) :

	l.append(dictionary[string[x:x+10]])

print ''.join(l)