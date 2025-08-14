x=list(map(int,input().split()))
x.sort()
s1=x[2]-x[1]
s2=x[1]-x[0]
print(s1+s2)