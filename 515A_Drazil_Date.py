a, b, s = map(int, raw_input().split())

if s >= (abs(a)+abs(b)) and (s - (abs(a)+abs(b)))%2 == 0 :

	print 'YES'

else :

	print 'NO'