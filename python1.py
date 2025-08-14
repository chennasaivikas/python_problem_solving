w = int(input("enter the no"))
if w % 2 == 0:
    if w / 2 == 0:
        print("YES")
    else:
        if ((w / 2) + 1 and (w / 2) - 1) == 0:
            print("YES")
else:
    print("NO")

