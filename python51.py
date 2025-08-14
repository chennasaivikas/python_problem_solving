n=int(input())
l=[]
for i in range(n):
    x=int(input())
    s=map(int,input().split())
    for i in range(x):
        for r in s:
            c=0
            if r==0:
                c+=1
            