s=input()
x=set(s)
count=0
for i in x:
    count+=1
if count%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")