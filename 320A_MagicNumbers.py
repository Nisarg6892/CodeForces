s = raw_input()
count = 0

count = count + s.count('144')
s = s.replace('144','$')

count = count + s.count('14')
s = s.replace('14','$')

count = count + s.count('1')
s = s.replace('1','$')

if len(s) == count :

	print 'YES'

else :

	print 'NO'