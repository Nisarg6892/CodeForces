L_or_R = raw_input()
string = raw_input()

line1 = 'qwertyuiop'
line2 = 'asdfghjkl;'
line3 = 'zxcvbnm,./'

final = []

for x in string :

	if x in line1 :

		if L_or_R == 'R' :
			
			final.append(line1[line1.index(x)-1])

		else :

			final.append(line1[line1.index(x)+1])

	if x in line2 :

		if L_or_R == 'R' :

			final.append(line2[line2.index(x)-1])

		else :

			final.append(line2[line2.index(x)+1])

	if x in line3 :

		if L_or_R == 'R' :

			final.append(line3[line3.index(x)-1])

		else :

			final.append(line3[line3.index(x)+1])			

print ''.join(final)
