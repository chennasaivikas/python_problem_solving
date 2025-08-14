t=int(input())
a=[]
for i in range(t):
    u=int(input())
    a.append(u)

qt=int(input())
for i in range(qt):
    l,r,x,y=(map(int,input().split()))
    
    for i in range(r-l+1):
        a[l+i]=x+y*i
print(sum(a))
    
