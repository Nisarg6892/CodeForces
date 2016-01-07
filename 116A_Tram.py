l=[]
result=0

for i in range(input()) :

	string_int = map(int,raw_input(). split())
	l.append(string_int[1]-string_int[0]+result)
	result=result+string_int[1]-string_int[0]

print max(l)