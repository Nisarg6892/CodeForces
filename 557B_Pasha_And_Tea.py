n, w = map(int, raw_input().split())
l = map(int, raw_input().split())

l.sort()

minimum_girl = min(l[:len(l)/2])
minimum_boy = min(l[len(l)/2:])

if minimum_girl*2 <= minimum_boy :

	x = 3 * minimum_girl * n

else :

	x = (minimum_boy + minimum_boy/2.0) * n

if x > w :

	x = w

print x