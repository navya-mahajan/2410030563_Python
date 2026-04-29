# Find the maximum and minimum elements in the array.
arr = [23,45,43,56,1,9]

max = arr[0]
min = arr[0]

for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i

print (f"Maximum Element: {max}, Minimum Element: {min}")

#reverse the array
arr = [1,2,3,4,5]
start = 0
end = len(arr) - 1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print(arr)

#kth smallest element in the array
arr = [10,5,4,3,48,6,2,33,53,10]
last = arr.pop()
k = arr.insert(0,last)
print(arr)

#union of two arrays
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 0]
c = [0] * (len(a) + len(b))
i =0
while i < len(a):
    c[i] = a[i]
    i += 1
j = 0
while j < len(b):
    c[i] = b[j]
    i += 1
    j += 1
print("Union of two arrays is:", c)

#largest element of the array
arr = [7, 10, 4, 3, 20, 15]
max = arr[0] 
for i in arr:  
    if i > max: 
        max = i
print("Largest element is:", max)

#rotating the array clockwise by one position
arr=[1, 2, 3, 4, 5]
a = arr.pop()
arr.insert(0, a)
print(arr)

# print maximum sum of the subarray
arr = [2, 3, -8, 7, -1, 2, 3]
max_sum = arr[0]
current_sum = 0
for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)
print(max_sum)

#return index of target value or where it would be if not in array
arr = [1, 3, 5, 6]
target = 5
while arr:
    mid = len(arr) // 2
    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] < target:
        arr = arr[mid + 1:]
    else:
        arr = arr[:mid]
else:
    print(len(arr))

#return indices of the two numbers such that they add up to target
nums = [3,2,4]
target = 6
def two_sum(nums, target):
   n = len(nums)
   for i in range(n):
      for j in range(i+1,n):
         if nums[i]+ nums[j] == target:
            return [i,j]
   return []
print(f"Result: {two_sum([3,2,4],6)}")

#find the minimum number of jumps to reach the end of the array
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
jumps = 0
current_end = 0
far = 0
for i in range(len(arr) - 1):
    far = max(far, i + arr[i])
    if i == current_end:
        jumps += 1
        current_end = far
print(jumps)
