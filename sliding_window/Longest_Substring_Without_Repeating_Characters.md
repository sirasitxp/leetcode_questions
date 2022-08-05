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

## Visualization
[Code Visualization](https://pythontutor.com/render.html#code=def%20lengthOfLongestSubstring%28s%3A%20str%29%3A%0A%20%20%20%20longest_streak%20%3D%200%0A%20%20%20%20l%20%3D%200%0A%20%20%20%20charSet%20%3D%20set%28%29%0A%20%20%20%20for%20r%20in%20range%28len%28s%29%29%3A%0A%20%20%20%20%20%20%20%20while%20s%5Br%5D%20in%20charSet%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20charSet.remove%28s%5Bl%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20l%20%2B%3D%201%0A%20%20%20%20%20%20%20%20charSet.add%28s%5Br%5D%29%0A%20%20%20%20%20%20%20%20longest_streak%20%3D%20max%28longest_streak,%20r-l%2B1%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20return%20longest_streak%0A%0AlengthOfLongestSubstring%28%22abcabcbb%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
