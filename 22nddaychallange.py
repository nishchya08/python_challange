# ignoring built-in Functions and Libraries

# inefficient
def custom_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
arr=[3,1,4,1,5,9]
sorted_arr = custom_sort(arr)
print(sorted_arr)

# Using Utilize Python's built-in function and libraries for optimized performance
# Efficient
arr=[3,1,4,1,5,9]
sorted_arr = sorted(arr)
print(sorted_arr)