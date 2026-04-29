#problem 1
import heapq

class Solution:
    def minOperations(self, arr):
        total = sum(arr)
        target = total / 2
        
        # max heap (use negative values)
        heap = [-x for x in arr]
        heapq.heapify(heap)
        
        ops = 0
        
        while total > target:
            x = -heapq.heappop(heap)
            
            reduced = x / 2
            total -= (x - reduced)
            
            heapq.heappush(heap, -reduced)
            ops += 1
        
        return ops

#problem 2
class Solution:
    def minMen(self, arr):
        n = len(arr)
        intervals = []
        
        # create coverage intervals
        for i in range(n):
            if arr[i] != -1:
                l = max(0, i - arr[i])
                r = min(n - 1, i + arr[i])
                intervals.append((l, r))
        
        intervals.sort()
        
        target = 0
        i = 0
        count = 0
        m = len(intervals)
        
        while target < n:
            farthest = -1
            
            while i < m and intervals[i][0] <= target:
                farthest = max(farthest, intervals[i][1])
                i += 1
            
            if farthest < target:
                return -1
            
            count += 1
            target = farthest + 1
        
        return count

#problem 3
class Solution:
    def prevSmaller(self, arr):
        stack = []
        res = []
        
        for x in arr:
            while stack and stack[-1] >= x:
                stack.pop()
            
            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)
            
            stack.append(x)
        
        return res

#problem 4
class Solution:
    def preGreaterEle(self, arr):
        stack = []
        res = []
        
        for x in arr:
            while stack and stack[-1] <= x:
                stack.pop()
            
            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)
            
            stack.append(x)
        
        return res

#problem 5
class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        next_smaller = [n] * n
        
        # Find next smaller element to the right
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                idx = stack.pop()
                next_smaller[idx] = i
            stack.append(i)
        
        ans = 0
        
        for i in range(n):
            ans += next_smaller[i] - i
        
        return ans

#problem 6
class Solution:
    def has132Pattern(self, arr):
        stack = []
        third = float('-inf')  # potential "2nd element in 132 pattern"
        
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] < third:
                return True
            
            while stack and arr[i] > stack[-1]:
                third = stack.pop()
            
            stack.append(arr[i])
        
        return False

#problem 7
class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        
        # nearest greater or equal on left
        left = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # nearest greater or equal on right
        right = [n] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        ans = 0
        
        for i in range(n):
            # correct visible count = span left + span right - 1 (avoid double counting self)
            visible = (i - left[i]) + (right[i] - i) - 1
            ans = max(ans, visible)
        
        return ans

#problem 8
class Solution:
    def combinationSum(self, n, k):
        res = []
        
        def backtrack(start, path, remaining, k_left):
            if remaining == 0 and k_left == 0:
                res.append(path[:])
                return
            
            if remaining < 0 or k_left < 0:
                return
            
            for i in range(start, 10):
                if i > remaining:
                    break
                
                path.append(i)
                backtrack(i + 1, path, remaining - i, k_left - 1)
                path.pop()
        
        backtrack(1, [], n, k)
        return res

#problem 9
class Solution:
    def equalPartition(self, arr):
        n = len(arr)
        total = sum(arr)
        
        # check if equal split possible
        # (must be even total sum)
        if total % 2 != 0:
            return []
        
        target = total // 2
        
        from itertools import combinations
        
        # required subset size
        if n % 2 == 0:
            sizes = [n // 2]
        else:
            sizes = [n // 2, n // 2 + 1]
        
        # try all valid sizes
        for size in sizes:
            for comb in combinations(range(n), size):
                s = sum(arr[i] for i in comb)
                
                if s == target:
                    subset1 = [arr[i] for i in comb]
                    subset2 = [arr[i] for i in range(n) if i not in comb]
                    return [subset1, subset2]
        
        return []

#problem 10
class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        
        def can_place(diff):
            count = 1
            last = arr[0]
            
            for i in range(1, len(arr)):
                if arr[i] - last >= diff:
                    count += 1
                    last = arr[i]
                    
                    if count == k:
                        return True
            
            return False
        
        low, high = 0, arr[-1] - arr[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans

#problem 11
class Solution:
    def countLessEqual(self, arr, x):
        count = 0
        
        for num in arr:
            if num <= x:
                count += 1
        
        return count

#problem 12
class Solution:
    def get_Sum(self, n, arr):
        total = 0
        
        for num in arr:
            total += num
        
        return total
