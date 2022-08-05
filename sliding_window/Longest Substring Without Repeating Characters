# Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Solution
1. Use Sliding Window 
2. Use set() to track duplicate characters

## Code
```python
def lengthOfLongestSubstring(self, s: str) -> int:
        longest_streak = 0
        l = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longest_streak = max(longest_streak, r-l+1)
        
        return longest_streak
```
