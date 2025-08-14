n=int(input())
g=input()
g=list(g)
if g.count("A")>g.count("D"):
    print("Anton")
elif g.count("A")<g.count("D"):
    print("Danik")
else:
    print("Friendship")