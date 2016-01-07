s = raw_input()
t = raw_input()
t_list = list(t)
t_list.sort()

YAY = 0
WHOOPS = 0

for x in s :

	if x in t_list :

		YAY = YAY + 1
		t_list.remove(x)

	elif x.swapcase() in t_list :

		WHOOPS = WHOOPS + 1
		t_list.remove(x.swapcase())

print str(YAY)+' '+str(WHOOPS)

