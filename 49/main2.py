from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            d[tuple(count)].append(s)
        return list(d.values())

if __name__ == '__main__':
    c = Solution()
    assert c.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']
    ]
    assert c.groupAnagrams([""]) == [[""]]
    assert c.groupAnagrams(["a"]) == [["a"]]