n,h=map(int,input().split())
l=[]
for i in range(1,n+1):
    if i%2!=0:
        print("#"*h)
    else:
        print("."*(h-1)+"#")


