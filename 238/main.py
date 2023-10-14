from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        length = len(nums) - 1
        res = [1] * len(nums)
        for i, n in enumerate(nums):
            if i == 0:
                prefix[i] = n
                postfix[length - i] = nums[length - i]
            else:
                prefix[i] = prefix[i -1] * nums[i]
                postfix[length - i] = nums[length - i] * postfix[length - i + 1]
        for i, n in enumerate(nums):
            if i == 0:
                res[i] = postfix[i + 1]
            elif i == length:
                res[i] = prefix[i - 1]
            else:
                res[i] = prefix[i - 1] * postfix[i + 1]
        return res
    

if __name__ == "__main__":
    c = Solution()
    assert [24,12,8,6] == c.productExceptSelf([1,2,3,4])
    