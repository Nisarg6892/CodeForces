m = int(raw_input())
h1, a1 = map(int, raw_input().split())
x1, y1 = map(int, raw_input().split())
h2, a2 = map(int, raw_input().split())
x2, y2 = map(int, raw_input().split())

TotalSeconds = 0
# list_h1 = [h1]
# list_h2 = [h2]
count = 0
Found = 0
	
while count <= 1000000 :

	h1 = (x1*h1+y1) % m

	# list_h1.append(h1)

	h2 = (x2*h2+y2) % m

	# if h1 in list_h1 and h2 in list_h2 :

	# 	TotalSeconds = -1
	# 	break

	# list_h2.append(h2)
	
	TotalSeconds = TotalSeconds + 1
	count = count + 1

	if h1 == a1 and h2 == a2 :

		Found = 1
		# print 'hi'
		break

if Found == 0 :

	TotalSeconds = -1

# print list_h1
# print list_h2
print TotalSeconds