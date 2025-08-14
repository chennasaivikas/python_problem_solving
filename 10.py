arr = [1,2,2,3,3,3]
for i in range(len(arr)):
    if arr[i]==arr.count(arr[i]):
        print(arr[i])
        break
    
