# 🔟Add Binary
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
## Explanation
1. First convert strings to lists, so that we can pop from the back.(No need to reverse)  
2. Run while loop to make sure that everything is exhausted.  
3. Keep popping from both of the list.
4. Add result of Mod to the result
5. Calculate the remaining carry by division.
6. After iterations, return reversed version of result as eveything was calculated from the back of the list.

## Analyze time and space complexity. 
```
Time: O(N)
Space: O(N)
```
