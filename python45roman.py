n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    c=(a-a)+(b-a)
    l.append(c)
for j in l:
    print(j)