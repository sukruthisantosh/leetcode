import math
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        minimum = float("inf")

        while l < r:
            m = l + ((r-l) // 2)
            print(f"m=", m)
            minimum = min(minimum, nums[m])
            print(f"minimum",minimum)
            print(f"nums", nums[m])
            if nums[m] > nums[r]:
                l = m + 1
                print(f"l=",l)
            else:
                r = m - 1
                print(f"r=",r)

        return min(minimum, nums[l])



solution = Solution()
nums = [4,5,6,7,0,1,2]
print(solution.findMin(nums=nums))