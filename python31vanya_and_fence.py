n,h=map(int,input().split())
m=(map(int,input().split()))
count=0
for i in (m):
    if i>h:
        count+=2
    else:
        count+=1
print(count)