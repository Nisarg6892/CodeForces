s = raw_input()
t = raw_input()
# s='aaaaaas'
# t='aaedacs'
new = []
count = 0

for x in range(0,len(s)):

	if s[x]==t[x]:
		new.append(s[x])
		count += 1

	else:

		for i in range(ord(s[x])+1,ord(t[x])):
			new.append(chr(i))
			count += 1
			break

		# break

if count == len(s) :
	print ''.join(new)

else :
	print 'No such string'

# print ord('ni')