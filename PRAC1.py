from collections import Counter
def grouping(nums):
    count=Counter(nums)
    nums.sort(key=lambda x : (-count[x],-x))
    return nums
arr=[1,1,2,3,3,3,4,4]
print(grouping(arr))