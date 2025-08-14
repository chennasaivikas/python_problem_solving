a=list(input())
b=list(input())
r=[]
for i in range(len(a)):
    if a[i]==b[i]:
        r.append("0")
    else:
        r.append("1")
print("".join(r))

