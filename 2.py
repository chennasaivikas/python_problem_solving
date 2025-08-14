n=int(input())
a=[]
s=0
for i in range(n):
    x=int(input())
    a.append(x)

q=int(input())

for i in range(q):
    t,l,r=map(int,input().split())
    if t==1:
        for i in range(l,r+1):
            a[i]=(a[i]+a[l]+1)*a[l]
    elif t==2:
        for i in range(l,r+1):
            s=s+a[i]

print(s)