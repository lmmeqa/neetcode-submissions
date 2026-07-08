class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = right = 0
        maxsum = 0
        for right in range(len(prices)):
            currsum = prices[right] - prices[left]
            maxsum = max(maxsum, currsum)
            if prices[right] < prices[left]:
                left = right
        return maxsum
            