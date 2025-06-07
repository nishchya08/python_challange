# python challanges
from pandas.io.formats.format import return_docstring

a=[1,2,3,4,5,6,7]
print(a[1:6:-1])

print("-----------------------------")

def unique_sums(nums):
    seen = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            seen.add(nums[i] + nums[j])
        return len(seen)
print(unique_sums([1,2,8,5,6,7,8,9]))