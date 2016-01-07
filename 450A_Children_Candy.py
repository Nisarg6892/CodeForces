n,m = map(int,raw_input().split())
l = raw_input().split()
# for x in range(0, n) :
s = ''.join(l)

print s.rindex(max(i for i in l))+1