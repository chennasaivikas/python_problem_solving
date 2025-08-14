n=int(input())
c=0
for i in range(n):
    x=input()
    if x=="Tetrahedron":
        c+=4
    elif x=="Cube":
        c+=6
    elif x=="Octahedron":
        c+=8
    elif x=="Dodecahedron":
        c+=12
    elif x=="Icosahedron":
        c+=20
    else:
        c-=1
print(c)
