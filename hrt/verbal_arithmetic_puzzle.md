# 🧩 Verbal Arithmetic Puzzle
Given an equation, represented by words on the left side and the result on the right side.

You need to check if the equation is solvable under the following rules:

Each character is decoded as one digit (0 - 9).
No two characters can map to the same digit.
Each words[i] and result are decoded as one number without leading zeros.
Sum of numbers on the left side (words) will equal to the number on the right side (result).
Return true if the equation is solvable, otherwise return false.

 

### Example 1:
```
Input: words = ["SEND","MORE"], result = "MONEY"
Output: true
Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
```
### Example 2:
```
Input: words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
Output: true
Explanation: Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
```
### Example 3:
```
Input: words = ["LEET","CODE"], result = "POINT"
Output: false
Explanation: There is no possible mapping to satisfy the equation, so we return false.
Note that two different characters cannot map to the same digit.
 ```

## Constraints:
```
2 <= words.length <= 5
1 <= words[i].length, result.length <= 7
words[i], result contain only uppercase English letters.
The number of different characters used in the expression is at most 10.
```

## Solution:
```python
from itertools import permutations
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        # we need begins set to track start letters if word is longer than one to not have them as 0
        begins = {result[0]} if len(result) > 1 else set()
        
        # the idea to have counter is to sum repeted letters based on where they are in the word
        
        c = Counter()
        for w in words:
            if len(w) > 1:
                begins.add(w[0])
            for i,l in enumerate(w[::-1]):
                c[l] += 10**i
        
        # we subtract "result" letters from the counter
        for i,l in enumerate(result[::-1]):
            c[l] -= 10**i
            
        # we get at the end something like that Counter({'S': 1000, 'E': 91, 'R': 10, 'D': 1, 'Y': -1, 'N': -90, 'O': -900, 'M': -9000})
        
        # lets split problem into 2 let's check positive letters and negative
        pos = []
        neg = []
        for l, v in c.items():
            if v > 0:
                pos.append( (l,v) )
            elif v < 0:
                neg.append( (l,-v) )

        if not neg and not pos:
            return True
        
        if not neg or not pos:
            # False if begins else True this one is needed for words with one letter like words = ["A","B"], result = "A"
            return False if begins else True
        
        NN = len(neg)
        NP = len(pos)
        
        # we need this one to process permutaion with the smaller number first
        # that would optimize speed
        if NN > NP:
            neg,pos = pos,neg
            NN,NP = NP, NN
        
        # we create dict with list of sets of permutations
        # keys sum of digit for letter * coefficient
        nd = defaultdict(list)
        for used in permutations(list(range(10)), NN):
            if 0 in used and neg[used.index(0)][0] in begins:
                continue
            nd[sum(v * used[i] for i,(l,v) in enumerate(neg))].append(set(used))
        
        # same for the other part
        # but while we are doing that we check if overlap of digits is missing
        for used in permutations(list(range(10)), NP):
            if 0 in used and pos[used.index(0)][0] in begins:
                continue
            s = sum(v * used[i] for i,(l,v) in enumerate(pos))
            s1 = set(used)
            if s in nd:
                for s2 in nd[s]:
                    if not s1 & s2:
                        return True

        return False

```
