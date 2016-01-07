n = int(raw_input())
l = map(int, raw_input().split())

count = l.count(4)
count_3 = l.count(3)
count_2 = l.count(2)
count_1 = l.count(1)

count = count + count_3

if count_3 < count_1 :

	count_1 = count_1 - count_3

else :

	count_1 = 0

count = count + ( count_2//2 )

count_2 = count_2 % 2

x = count_2*2 + count_1

if x % 4 != 0 :

	count = count + ( x//4 ) + 1

else :

	count = count + x//4

print count