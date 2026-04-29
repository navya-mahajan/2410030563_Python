#problem 1
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

#problem 2
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def dfs(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                dfs(i, remaining - candidates[i])  # i (not i+1) allows reuse
                path.pop()

        dfs(0, target)
        return res

#problem 3
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                dfs(i + 1, remaining - candidates[i])
                path.pop()

        dfs(0, target)
        return res

#problem 4
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps

#problem 5
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            res[key].append(s)

        return list(res.values())

#problem 6
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

#problem 7
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        firstRowZero = any(matrix[0][j] == 0 for j in range(n))
        firstColZero = any(matrix[i][0] == 0 for i in range(m))

        # mark using first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # set cells to zero based on marks
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # handle first row
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0
  
        # handle first column
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0

#problem 8
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

#problem 9
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid = 0, 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

#problem 10
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(index):
            # add current subset
            res.append(path[:])

            for i in range(index, len(nums)):
                path.append(nums[i])     # choose
                dfs(i + 1)               # explore
                path.pop()               # backtrack

        dfs(0)
        return res

#problem 11
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            # k = current index in word
            if k == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if board[i][j] != word[k]:
                return False

            # mark visited
            temp = board[i][j]
            board[i][j] = "#"

            # explore all 4 directions
            found = (
                dfs(i + 1, j, k + 1) or
                dfs(i - 1, j, k + 1) or
                dfs(i, j + 1, k + 1) or
                dfs(i, j - 1, k + 1)
            )

            # backtrack
            board[i][j] = temp

            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False

#problem 12
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res

#problem 13
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

#problem 14
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findFirst():
            left, right = 0, len(nums) - 1
            res = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                
                if nums[mid] == target:
                    res = mid
            
            return res
        
        def findLast():
            left, right = 0, len(nums) - 1
            res = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                
                if nums[mid] == target:
                    res = mid
            
            return res
        
        return [findFirst(), findLast()]
