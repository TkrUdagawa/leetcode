from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[str(n)] += 1
        l = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return [int(x[0]) for x in l[:k]]
            
            


if __name__ == "__main__":
    c = Solution()
    assert [1, 2] == c.topKFrequent([1,1,1,2,2,3], k=2)
