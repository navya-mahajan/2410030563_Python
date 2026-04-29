#probelm 1
class Solution:
    def minSwaps(self, s1, s2):
        a = 0
        b = 0
        
        n = len(s1)
        
        for i in range(n):
            if s1[i] == '0' and s2[i] == '1':
                a += 1
            elif s1[i] == '1' and s2[i] == '0':
                b += 1
        
        # impossible case
        if (a + b) % 2 != 0:
            return -1
        
        # correct formula
        return (a // 2) + (b // 2) + (a % 2 + b % 2)

#problem 2
class Solution:
    def minParentheses(self, s):
        open_needed = 0
        add = 0
        
        for ch in s:
            if ch == '(':
                open_needed += 1
            else:
                if open_needed > 0:
                    open_needed -= 1
                else:
                    add += 1
        
        return add + open_needed

#problem 3
class Solution:
    def scoreOfParentheses(self, s):
        stack = [0]
        
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                val = stack.pop()
                if val == 0:
                    val = 1
                else:
                    val *= 2
                stack[-1] += val
        
        return stack[0]

#problem 4
class Solution:
    def minDifference(self, arr):
        def to_seconds(t):
            h, m, s = map(int, t.split(":"))
            return h * 3600 + m * 60 + s
        
        n = len(arr)
        times = [to_seconds(t) for t in arr]
        
        times.sort()
        
        min_diff = float('inf')
        
        # adjacent differences
        for i in range(1, n):
            min_diff = min(min_diff, times[i] - times[i - 1])
        
        # circular difference (wrap around midnight)
        wrap = (24 * 3600 - times[-1]) + times[0]
        min_diff = min(min_diff, wrap)
        
        return min_diff

#problem 5
class Solution:
    def frequencySort(self, s):
        from collections import Counter
        
        freq = Counter(s)
        
        # sort by (frequency, character)
        sorted_chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))
        
        result = []
        for ch, f in sorted_chars:
            result.append(ch * f)
        
        return "".join(result)

#problem 6
class Solution:
    def sortByLength(self, arr):
        arr.sort(key=len)
        return arr

#problem 7
class Solution:
    def countPairs(self, arr):
        from collections import defaultdict
        
        n = len(arr)
        m = len(arr[0])
        ans = 0
        
        # try removing each position
        for i in range(m):
            freq = defaultdict(int)
            
            for s in arr:
                key = s[:i] + s[i+1:]
                ans += freq[key]
                freq[key] += 1
        
        return ans

#problem 8
class Solution:
    def winner(self, arr):
        freq = {}
        
        # count votes
        for name in arr:
            freq[name] = freq.get(name, 0) + 1
        
        max_votes = 0
        winner_name = ""
        
        # find winner
        for name in freq:
            if freq[name] > max_votes:
                max_votes = freq[name]
                winner_name = name
            elif freq[name] == max_votes:
                if name < winner_name:
                    winner_name = name
        
        return [winner_name, str(max_votes)]

#problem 9
class Solution:
    def search(self, txt, pat):
        n, m = len(txt), len(pat)
        
        if m > n:
            return False
        
        # frequency arrays for 26 letters
        pat_freq = [0] * 26
        win_freq = [0] * 26
        
        # build pattern frequency
        for ch in pat:
            pat_freq[ord(ch) - ord('a')] += 1
        
        # first window
        for i in range(m):
            win_freq[ord(txt[i]) - ord('a')] += 1
        
        if win_freq == pat_freq:
            return True
        
        # slide window
        for i in range(m, n):
            win_freq[ord(txt[i]) - ord('a')] += 1
            win_freq[ord(txt[i - m]) - ord('a')] -= 1
            
            if win_freq == pat_freq:
                return True
        
        return False

#problem 10
class Solution:
    def maxSubseq(self, s, k):
        stack = []
        
        for ch in s:
            while stack and k > 0 and stack[-1] < ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        
        # remove remaining k from end
        while k > 0:
            stack.pop()
            k -= 1
        
        return "".join(stack)

#problem 11
class Solution:
    def vowelCount(self, s):
        vowels = "aeiou"
        freq = {}
        
        # Count vowel frequencies
        for ch in s:
            if ch in vowels:
                freq[ch] = freq.get(ch, 0) + 1
        
        k = len(freq)
        if k == 0:
            return 0
        
        # factorial
        fact = 1
        for i in range(2, k + 1):
            fact *= i
        
        # product of frequencies
        prod = 1
        for v in freq.values():
            prod *= v
        
        return prod * fact

#problem 12
from collections import Counter

class Solution:
    def count(self, s):
        freq = Counter(s)
        return sum(1 for v in freq.values() if v % 2 == 0)

#problem 13
class Solution:
    def substrWithVowels(self, s1, s2):
        required = set(s1)
        freq = {}
        
        left = 0
        formed = 0
        min_len = float('inf')
        
        for right in range(len(s2)):
            ch = s2[right]
            
            if ch in required:
                freq[ch] = freq.get(ch, 0) + 1
                if freq[ch] == 1:
                    formed += 1
            
            while formed == len(required):
                min_len = min(min_len, right - left + 1)
                
                left_char = s2[left]
                if left_char in required:
                    freq[left_char] -= 1
                    if freq[left_char] == 0:
                        formed -= 1
                
                left += 1
        
        return min_len if min_len != float('inf') else -1

#problem 14
class Solution:
    def is_vowel(self, c):
        return c in "aeiou"
    
    def countBalanced(self, arr):
        val = []
        
        for s in arr:
            vowels = sum(1 for ch in s if self.is_vowel(ch))
            consonants = len(s) - vowels
            val.append(vowels - consonants)
        
        prefix = 0
        ans = 0
        mp = {0: 1}
        
        for x in val:
            prefix += x
            if prefix in mp:
                ans += mp[prefix]
            mp[prefix] = mp.get(prefix, 0) + 1
        
        return ans   # ✅ only return, no print
