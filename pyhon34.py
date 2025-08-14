n=int(input())
m=map(int,input().split(" "))
X=list(m)
if X.count(1)>=1:
    print("HARD")
else:
    print("EASY")

