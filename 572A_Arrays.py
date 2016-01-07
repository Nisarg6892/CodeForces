nA, nB = map(int, raw_input().split())
k, m = map(int, raw_input().split())

A = map(int, raw_input().split())
B = map(int, raw_input().split())

first = A[k-1]
second = B[m*-1]

if first < second :

	print 'YES'

else :

	print 'NO'
# a = [1,2,3]
# print a[-1:-3:-1]