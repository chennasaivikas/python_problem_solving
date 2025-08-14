
x=[2,3,7,5,1,4,6,8,9]
sum=0
for i in range(len(x)):
    if i%2==1:
        if x[i]%2==0:
            sum+=x[i]
print(sum)
