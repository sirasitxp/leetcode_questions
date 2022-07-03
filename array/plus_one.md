# Plus One
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

## Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

## Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

## Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

## Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

# Solution
Iterate through the array from the back, check if each number is equal to nine, if so set it to zero and increase the number in front of it by one. 

## Code Example
```python
def plusOne(digits):
        n = len(digits)
        for i in range(n):
            idx = n - 1 - i
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits
        return [1] + digits
```
## Code Visualization
https://pythontutor.com/render.html#code=def%20plusOne%28digits%29%3A%0A%20%20%20%20%20%20%20%20n%20%3D%20len%28digits%29%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28n%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20idx%20%3D%20n%20-%201%20-%20i%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20digits%5Bidx%5D%20%3D%3D%209%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20digits%5Bidx%5D%20%3D%200%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20digits%5Bidx%5D%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20digits%0A%20%20%20%20%20%20%20%20return%20%5B1%5D%20%2B%20digits%0A%20%20%20%20%20%20%20%20%0Aprint%28plusOne%28%5B1,2,3%5D%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

## Analyzing time and space complexity.
Time: O(N).  
Space: O(N).  
