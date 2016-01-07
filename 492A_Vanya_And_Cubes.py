n = int(raw_input())
Sum = 0
i = 0
total = 0
count = 0

while total < n :

	i = i + 1
	Sum = Sum + i
	total = total + Sum

	if total <= n :
		
		count = count + 1

print count
