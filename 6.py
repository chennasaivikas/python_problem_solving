x=input()
if x=="{}":
    print(0)
else:
    x=x.strip("{}")
    x=x.split(", ")
    print(len(set(x)))