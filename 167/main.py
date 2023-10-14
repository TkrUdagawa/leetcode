from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1
        while True:
            s = numbers[head] + numbers[tail]
            if  s == target:
                return [head + 1, tail + 1]
            elif s < target:
                head += 1
            else:
                tail -= 1
                
    

if __name__ == "__main__":
    c = Solution()
    assert [1, 2] == c.twoSum([2,7,11,15], 9)
