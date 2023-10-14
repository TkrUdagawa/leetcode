from typing import List, Dict
    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tree = {}
        num_set = set(nums)
        max_length = 0
        for n in num_set:
            length = 1
            if n - 1 not in num_set:
                while n + 1 in num_set:
                    length += 1
                    n += 1
            if length > max_length:
                max_length = length               
        return max_length
        
        
    
    
if __name__ == "__main__":
    c = Solution()
    assert 4 == c.longestConsecutive([100, 4, 200, 1, 3, 2])
    assert 9 == c.longestConsecutive([0,3,7,2,5,8,4,6,0,1])