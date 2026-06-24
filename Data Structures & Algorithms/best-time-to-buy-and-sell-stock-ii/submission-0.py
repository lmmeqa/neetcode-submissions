class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for day, value in enumerate(prices):
            if day+1 == len(prices):
                continue
            if value < prices[day + 1]:
                profit+= prices[day+1] - value
        return profit
        