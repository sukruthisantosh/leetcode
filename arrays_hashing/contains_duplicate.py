from math import trunc
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


solution = Solution()
nums = [1,2,3,1]
print(solution.containsDuplicate(nums=nums))