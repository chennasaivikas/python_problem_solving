t=int(input())

for i in range(t):
    l=[]
    l2=[]
    x=(input())
    for i in x:
        l.append(i)
    lis=list(map(int,l))

    if (lis[0]+lis[1]+lis[2])==(lis[3]+lis[4]+lis[5]):
        l2.append("YES")
    else:
        l2.append("NO")
for i in l2:
    print(i)

