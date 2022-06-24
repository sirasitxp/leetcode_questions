from collections import defaultdict
def groupAnagrams(strs):
        res = defaultdict(list)
        for word in strs:
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            res[tuple(char_count)].append(word)

        return res.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))