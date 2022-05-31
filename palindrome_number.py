"""
Palindrome Number

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore, it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?

"""

def isPalindrome(x: int) -> bool:
    x = str(x)
    left = 0
    right = len(x) - 1
    while (left <= right):
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindrome_no_conversion(x: int) -> bool:
    if x < 0:
        return False
    original = x
    reverse = remainder = 0
    while (x != 0):
        remainder = x % 10
        reverse = (reverse * 10) + remainder
        x = x // 10
    if -2 ** 31 > reverse > 2 ** 31 - 1:
        return False
    return original == reverse


print(isPalindrome(123))
print(isPalindrome_no_conversion(121))