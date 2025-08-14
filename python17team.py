
p=int(input())
count=0
for i in range(p):
    a,b,c=map(int,input().split())
    if (a,b,c).count(1)>=2:
        count+=1
print(count)