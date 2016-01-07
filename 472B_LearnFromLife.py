n,k = map(int,raw_input().split())

Floor_History = raw_input()
Floor_History_list_int = map(int,Floor_History.split())
Floor_History_list_int.sort(reverse = True)
ans = 0

while Floor_History_list_int :
	
	ans = ans + (max(Floor_History_list_int[0:k])-1)*2
	# print ans
	Floor_History_list_int[:] = Floor_History_list_int[k:n]
	# print Floor_History_list_int

print ans


