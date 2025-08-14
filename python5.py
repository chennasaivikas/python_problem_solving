L,B=map(int, input().split())
c=0
while B>=L:
    L=L*3
    B=B*2
    c=c+1
print(c)