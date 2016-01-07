import sys
count=0
ans=0

for x in sys.stdin:

	if x[0] == '+' :
		count +=1

	elif x[0] == '-':
		count-=1

	else:
		ans+=(len(x))*count

print ans
