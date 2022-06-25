# Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

## Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

## Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

## Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

# Solution
Go through the array one-pass. Check with if/elif conditions if any of them are equal to 0 or 2, if so move the zeros to the left, regarding to left pointer. Do the opposite for twos. So that, all the ones will end up in the middle. 

# Code example:


# Code Visualization:
https://pythontutor.com/render.html#code=def%20sortColors%28nums%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20Do%20not%20return%20anything,%20modify%20nums%20in-place%20instead.%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20l,%20r%20%3D%200,%20len%28nums%29-1%0A%20%20%20%20%20%20%20%20i%20%3D%200%0A%20%20%20%20%20%20%20%20while%20i%20%3C%3D%20r%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20nums%5Bi%5D%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20nums%5Bl%5D,%20nums%5Bi%5D%20%3D%20nums%5Bi%5D,%20nums%5Bl%5D%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20l%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20nums%5Bi%5D%20%3D%3D%202%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20nums%5Br%5D,%20nums%5Bi%5D%20%3D%20nums%5Bi%5D,%20nums%5Br%5D%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20r%20-%3D%201%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20i%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20i%20%2B%3D%201%0A%0Anums%20%3D%20%5B2,0,2,1,1,0%5D%0AsortColors%28nums%29%0Aprint%28nums%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
