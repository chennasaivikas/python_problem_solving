n=int(input())
l=[]
for i in range(n):
    x=int(input())
    if x<=1399:
        l.append("Division 4")
    elif 1400<=x<=1599:
        l.append("Division 3")
    elif 1600<=x<=1899:
        l.append("Division 2")
    elif 1900<=x:
        l.append("Division 1")
    else:
        l.append(-1)
for i in l:
    print(i)