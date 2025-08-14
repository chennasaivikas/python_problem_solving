n,m=map(int,input().split())
s=n*m
for i in range(s):
    if i*n==s:
        print(i)
        break