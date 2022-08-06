# Longest Repeating Character Replacement
## Code example
```python
def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        maxf = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            
            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            longest =  max(longest, (r-l+1))
        return longest
```
