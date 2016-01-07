s = raw_input()
t = raw_input()
dictionary_s = {}
dictionary_t = {}
YAY = 0
WHOOPS = 0

for x in s :

	dictionary_s[x] = dictionary_s.get(x, 0) + 1

for x in t :

	dictionary_t[x] = dictionary_t.get(x, 0) + 1

t_keys_list = dictionary_t.keys()

for x in dictionary_s :

	if x in t_keys_list :

		minimum = min(dictionary_s[x],dictionary_t[x])
		YAY = YAY + minimum
		dictionary_t[x] = dictionary_t[x] - minimum
		dictionary_s[x] = dictionary_s[x] - minimum

for x in dictionary_s :

	if dictionary_s[x] > 0 :

		if x.swapcase() in t_keys_list :

			minimum = min(dictionary_s[x],dictionary_t[x.swapcase()])
			WHOOPS = WHOOPS + minimum

print YAY, WHOOPS