# square root of smallest perfect square number if not avaliable then return 0

n=int(input())
l=[]
for k in range(n):
    x=int(input())
    l.append(x)
l.sort()
for j in l:
    if k**k in l:
        print(k)
    else:
        continue

