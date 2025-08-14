n=int(input())
r=0
for i in range(n):
    p,q=map(int,input().split())
    if p<q:
        if (q-p)>=2:
            r+=1
    else:
        r+=0
print(r)