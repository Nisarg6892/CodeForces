n = raw_input()
# n='77'
n=n.replace('4','0').replace('7','1')

length = len(n)
ans = 0

for x in range(1,length) :

	ans = ans + 2**x

print ans+int(n,2)+1