n = int(raw_input())

d = { 5:'Sheldon', 4:'Leonard', 3:'Penny', 2:'Rajesh', 1:'Howard' }

length = 5
Sum = 5
count = 1

while length < n :

	Sum = Sum * 2
	length = length + Sum
	count = count * 2

print d[(length-(n-1)+(count-1))//count]