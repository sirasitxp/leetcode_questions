# Permutation in string
```python
def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for n in range(26):
            matches += (1 if s1Count[n] == s2Count[n] else 0)
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if (s2Count[index] == s1Count[index]):
                matches += 1
            elif s2Count[index] == s1Count[index] +1:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] -1:
                matches -=1
            l += 1
        return matches ==26
```
## Code Visualization
[Code Visualization](https://pythontutor.com/render.html#code=def%20checkInclusion%28s1%3A%20str,%20s2%3A%20str%29%3A%0A%20%20%20%20%20%20%20%20if%20len%28s1%29%20%3E%20len%28s2%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%20%20%20%20s1Count,%20s2Count%20%3D%20%5B0%5D%20*%2026,%20%5B0%5D%20*%2026%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28len%28s1%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20s1Count%5Bord%28s1%5Bi%5D%29%20-%20ord%28'a'%29%5D%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20s2Count%5Bord%28s2%5Bi%5D%29%20-%20ord%28'a'%29%5D%20%2B%3D%201%0A%20%20%20%20%20%20%20%20matches%20%3D%200%0A%20%20%20%20%20%20%20%20for%20n%20in%20range%2826%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20matches%20%2B%3D%20%281%20if%20s1Count%5Bn%5D%20%3D%3D%20s2Count%5Bn%5D%20else%200%29%0A%20%20%20%20%20%20%20%20l%20%3D%200%0A%20%20%20%20%20%20%20%20for%20r%20in%20range%28len%28s1%29,%20len%28s2%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20matches%20%3D%3D%2026%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20index%20%3D%20ord%28s2%5Br%5D%29%20-%20ord%28'a'%29%0A%20%20%20%20%20%20%20%20%20%20%20%20s2Count%5Bindex%5D%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20%28s2Count%5Bindex%5D%20%3D%3D%20s1Count%5Bindex%5D%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matches%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20s2Count%5Bindex%5D%20%3D%3D%20s1Count%5Bindex%5D%20%2B1%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matches%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20index%20%3D%20ord%28s2%5Bl%5D%29%20-%20ord%28'a'%29%0A%20%20%20%20%20%20%20%20%20%20%20%20s2Count%5Bindex%5D%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20s2Count%5Bindex%5D%20%3D%3D%20s1Count%5Bindex%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matches%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20s2Count%5Bindex%5D%20%3D%3D%20s1Count%5Bindex%5D%20-1%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matches%20-%3D1%0A%20%20%20%20%20%20%20%20%20%20%20%20l%20%2B%3D%201%0A%20%20%20%20%20%20%20%20return%20matches%20%3D%3D26%0A%0AcheckInclusion%28'ba',%20'ab'%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
