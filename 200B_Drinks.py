# from __future__ import divison

n = int(raw_input())
string_int = map(int, raw_input().split())

sum = 0

for x in string_int :

    sum += x
    
print float(sum)/n