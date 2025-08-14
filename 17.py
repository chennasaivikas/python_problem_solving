t=int(input())
l=[]
for i in range(t):
    a,b,c=map(int,input().split())
    if a+b==c:
        l.append("+")
    else:
        l.append("-")

for i in l:
    print(i)