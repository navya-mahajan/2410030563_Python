# problem 1
def min_chocolate_difference(arr, m):
    n = len(arr)
    if m == 0 or n == 0:
        return 0
    arr.sort()
    if n < m:
        return -1
    min_diff = float('inf')
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)
    return min_diff
print(min_chocolate_difference([3, 4, 1, 9, 56, 7, 9, 12], 5)) 

#problem 2
def smallest_subarray_sum(arr, x):
    n = len(arr)
    min_len = n + 1
    curr_sum = 0
    start = 0
    for end in range(n):
        curr_sum += arr[end]
        while curr_sum > x:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1
    return 0 if min_len == n + 1 else min_len
print(smallest_subarray_sum([1, 4, 45, 6, 0, 19], 51))  

#problem 3
def three_way_partition(arr, a, b):
    n = len(arr)
    low, mid, high = 0, 0, n - 1
    while mid <= high:
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] > b:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1
    return True  # Successfully partitioned
arr1 = [1, 2, 3, 3, 4]
print(three_way_partition(arr1, 1, 2), arr1)  

#problem 4
def min_swaps(arr, k):
    n = len(arr)
    count = sum(1 for x in arr if x <= k)
    if count == 0 or count == n:
        return 0
    bad = sum(1 for x in arr[:count] if x > k)
    ans = bad
    for i in range(count, n):
        if arr[i - count] > k:
            bad -= 1
        if arr[i] > k:
            bad += 1
        ans = min(ans, bad)
    return ans
print(min_swaps([2, 1, 5, 6, 3], 3))     

#problem 5
def all_palindromes(arr):
    for num in arr:
        s = str(num)
        if s != s[::-1]:
            return False
    return True
print(all_palindromes([111, 222, 333, 444, 555])) 

#problem 6
def find_median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
print(find_median([90, 100, 78, 89, 67]))  

# problem 7
def spiral_order(mat):
    result = []
    if not mat:
        return result
    top, bottom = 0, len(mat) - 1
    left, right = 0, len(mat[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(mat[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(mat[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1
    return result
mat1 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
print(spiral_order(mat1))

#problem 8
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    n, m = len(matrix), len(matrix[0])
    left, right = 0, n * m - 1
    while left <= right:
        mid = (left + right) // 2
        row, col = divmod(mid, m)
        mid_val = matrix[row][col]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  

# problem 9
import bisect
def matrix_median(mat):
    n = len(mat)
    m = len(mat[0])
    min_val = min(row[0] for row in mat)
    max_val = max(row[-1] for row in mat)
    desired = (n * m + 1) // 2 
    while min_val < max_val:
        mid = (min_val + max_val) // 2
        count = 0
        for row in mat:
            count += bisect.bisect_right(row, mid)
        if count < desired:
            min_val = mid + 1
        else:
            max_val = mid
    return min_val
mat1 = [[1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]]
print(matrix_median(mat1))  

# problem 10
def row_with_max_1s(arr):
    n = len(arr)
    m = len(arr[0]) if n > 0 else 0
    row_index = -1
    j = m - 1
    for i in range(n):
        while j >= 0 and arr[i][j] == 1:
            row_index = i
            j -= 1
    return row_index
print(row_with_max_1s([[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]])) 
