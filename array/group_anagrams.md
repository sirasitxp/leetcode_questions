# Group Anagram
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


## Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"].  
Output: [["bat"],["nat","tan"],["ate","eat","tea"]].  

## Example 2:

Input: strs = [""].  
Output: [[""]].  

## Example 3:

Input: strs = ["a"]   
Output: [["a"]].  
 

## Constraints:

1 <= strs.length <= 104.  
0 <= strs[i].length <= 100.  
strs[i] consists of lowercase English letters.


# Solution
The most optimal solution is to create an array that represents number of characters at each index. For instance, if the array at index 0 stores 4 as a value, that means a word in a string contains 4 a's in it. Use this process to track how many characters are there in a word, add them to corresponding key in a hasmap. 

## Code example:
```python
from collections import defaultdict
def groupAnagrams(strs):
        res = defaultdict(list)
        for word in strs:
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            res[tuple(char_count)].append(word)

        return res.values()
```

## Analyzing time and space complexity
Time: O(M*N) where m is the size of the input and n is the size of each word  
Space: O(N) since there is only 1 hashmap required
