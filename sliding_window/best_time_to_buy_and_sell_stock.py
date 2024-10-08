from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        max_profit = 0

        for price in prices[1:]:
            minimum = min(price, minimum)
            max_profit = max(max_profit, price - minimum)

        return max_profit




solution = Solution()
prices = [7,1,5,3,6,4]
print(solution.maxProfit(prices=prices))