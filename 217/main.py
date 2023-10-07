from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True


if __name__ == "__main__":
    c = Solution()
    assert c.containsDuplicate([1,2,3,1])
    assert not c.containsDuplicate([1,2,3,4])
    assert c.containsDuplicate([1,1,1,3,3,4,3,2,4,2])

    