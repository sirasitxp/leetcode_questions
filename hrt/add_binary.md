# 1️🔟 Add Binary
Given two binary strings a and b, return their sum as a binary string.

 

### Example 1:
```
Input: a = "11", b = "1"  
Output: "100"  
```
### Example 2:  
```
Input: a = "1010", b = "1011"
Output: "10101"
```
## Constraints:
1 <= a.length, b.length <= 104  
a and b consist only of '0' or '1' characters.   
Each string does not contain leading zeros except for the zero itself.  
 
# Solution
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]
```
