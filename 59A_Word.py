s=raw_input()

UpperCount=0
LowerCount=0

for i in s:

	if i.isupper():
		
		UpperCount+=1

	else :

		LowerCount+=1

if UpperCount>LowerCount :

	print s.upper()

else :

	print s.lower()
