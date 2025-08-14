n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=x.sort(reverse=True)
r=y.sort(reverse=True)

if  z[0]>=4 or r[0]>=4 :
    print("I become the guy.")
else:
    print("Oh, my keyboard!")