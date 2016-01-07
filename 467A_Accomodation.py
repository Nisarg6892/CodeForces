n=int(raw_input())
count = 0

for i in range(0,n):
    string = raw_input()
    l=map(int,string.split())
    
    if l[1]-l[0]>=2:
        count+=1

print count