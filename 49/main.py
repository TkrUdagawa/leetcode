from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        return list(d.values())

if __name__ == '__main__':
    c = Solution()
    assert c.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']
    ]
    assert c.groupAnagrams([""]) == [[""]]
    assert c.groupAnagrams(["a"]) == [["a"]]