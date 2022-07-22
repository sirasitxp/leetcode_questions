# Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.   
You must write an algorithm that runs in O(n) time.

## Example 1:
Input: nums = [100,4,200,1,3,2]   
Output: 4   
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.   

## Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

## Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109

# Solution
Copy a set ,iterate through the array, check if it is a starting point of a sequence. If it is, check if it has more values next to it. 

# Code Example:
```python
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest  
```

# Analyzing time and space complexity
Time: O(N)   
Space: O(N)

# Code Visualization
https://pythontutor.com/render.html#code=def%20longestConsecutive%28nums%29%20-%3E%20int%3A%0A%20%20%20%20numSet%20%3D%20set%28nums%29%0A%20%20%20%20longest%20%3D%200%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20for%20n%20in%20nums%3A%0A%20%20%20%20%20%20%20%20if%20%28n-1%29%20not%20in%20numSet%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20length%20%3D%200%0A%20%20%20%20%20%20%20%20%20%20%20%20while%20%28n%2Blength%29%20in%20numSet%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20length%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20longest%20%3D%20max%28length,%20longest%29%0A%20%20%20%20return%20longest%20%20%0A%20%20%20%20%20%20%20%20%0Aprint%28longestConsecutive%28%5B100,4,200,1,3,2%5D%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
