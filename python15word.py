s=input()
lower_count=0
u_c=0
for i in s:
    if i==i.lower():
        lower_count+=1
    else:
        u_c+=1
if lower_count>u_c:
    print(s.lower())
elif u_c>lower_count:
    print(s.upper())
else:
    print(s.lower())
        
