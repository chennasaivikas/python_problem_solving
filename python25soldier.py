k,n,w=map(int,input().split())
sum=0
for i in range(w+1):
    sum=sum+(k*i)
if sum>=n:
    print(sum-n)
else:
    print(0)