n, x = map(int, raw_input().split())
l = map(int, raw_input().split())
Sum = 0

for y in l :

	Sum = Sum + y

Sum = abs(Sum)

print ( Sum + (x-1) ) // x