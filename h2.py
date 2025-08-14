t=int(input())
A=[]
sum1=0

for _ in range(t):
    n=int(input())
    A.append(n)

q=int(input())
for _ in range(q):
    x,l,r=list(map(int,input().split()))

    if x==1:
        for i in range(l,r+1):
            A[i]=(i-l+1)*A[l]
    elif x==2:
        sum1=sum1+sum(A[l:r+1])

print(sum1)
