x=(input())
y=(input())

s1=x.lower()
s2=y.lower()

if s1==s2:
    print(0)
elif s1>s2:
    print(1)
else:
    print(-1)