nums=[0,0,1,1,1,2,2,3,3,4]
s=set(nums)
d=len(nums)-len(s)
l=list(s)
for i in range(d):
    l.append('_')
print(l)
