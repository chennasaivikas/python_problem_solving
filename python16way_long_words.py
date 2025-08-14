t=int(input())
for i in range(t):
    w=input()
    count=len(w)
    if count<10:
        print(w)
    else:
        print(w[0]+str(count-2)+w[-1])

