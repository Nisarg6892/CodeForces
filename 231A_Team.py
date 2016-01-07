count = 0

for x in range(input()) :
    
    string = raw_input()
    string_int = map(int,string.split())
    
    sum = 0
    
    for x in string_int :
    
	    sum = sum + x
    
    if sum >= 2 :
    
	    count += 1
        
print count