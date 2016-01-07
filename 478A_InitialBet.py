sum = 0
string_int = map(int,raw_input().split())

for x in string_int :
    sum += x

if sum % 5 == 0:
    print sum/5
    
else :
    print '-1'