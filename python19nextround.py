n,k=map(int,input().split())
m=map(int,input().split())
count=0
for i in m:
    if i>k and +i:
        count+=1
print(count)


n, k = map(int, input().split())
m = list(map(int, input().split()))
count = 0

threshold = m[k - 1]

for i in m:
    if i >= threshold and i > 0:
        count += 1

print(count)
