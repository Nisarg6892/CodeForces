k = int(raw_input())
l = int(raw_input())
m = int(raw_input())
n = int(raw_input())
d = int(raw_input())

lis=[]

for x in range(1,d+1) :

	if x % k == 0 :

		lis.append(x)

	if l % k != 0 :
		
		if x % l == 0 :

			lis.append(x)

	if m % k != 0 or m % l != 0 :
		
		if x % m == 0 :

			lis.append(x)

	if n % k != 0 or n % l != 0 or n % m != 0 :
		
		if x % n == 0 :

			lis.append(x)

print len(set(lis))