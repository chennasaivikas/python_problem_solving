b_h=[2,3,4,3,2,3,5,4,2]
light=0
count=0
for i in b_h:
    if i>light:
        light=i
        count+=1
print(count)
