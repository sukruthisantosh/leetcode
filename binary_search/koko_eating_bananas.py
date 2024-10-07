from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        final_speed = r

        while l <= r:
            speed = (l + r) // 2
            total_hours = 0
            for pile in piles:
                total_hours += ceil(float(pile)/speed)
            if total_hours <= h:
                final_speed = speed
                r = speed - 1
            else:
                l = speed + 1
        return final_speed










solution = Solution()
piles = [3,6,7,11]
h = 8
print(solution.minEatingSpeed(piles=piles, h=h))



