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
## Code Visualization
[Code Visualization](https://pythontutor.com/render.html#code=def%20characterReplacement%28s%3A%20str,%20k%3A%20int%29%3A%0A%20%20%20%20longest%20%3D%200%0A%20%20%20%20l%20%3D%200%0A%20%20%20%20maxf%20%3D%200%0A%20%20%20%20count%20%3D%20%7B%7D%0A%20%20%20%20for%20r%20in%20range%28len%28s%29%29%3A%0A%20%20%20%20%20%20%20%20count%5Bs%5Br%5D%5D%20%3D%201%20%2B%20count.get%28s%5Br%5D,%200%29%0A%20%20%20%20%20%20%20%20maxf%20%3D%20max%28maxf,%20count%5Bs%5Br%5D%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20while%20%28r-l%2B1%29%20-%20maxf%20%3E%20k%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20count%5Bs%5Bl%5D%5D%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20l%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20longest%20%3D%20%20max%28longest,%20%28r-l%2B1%29%29%0A%20%20%20%20return%20longest%0A%0AcharacterReplacement%28%22ABAB%22,%202%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
