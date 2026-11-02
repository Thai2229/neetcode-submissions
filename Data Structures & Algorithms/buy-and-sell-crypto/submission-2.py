class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestLow = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, prices[i] - bestLow)
            bestLow = min(bestLow, prices[i])

        return maxProfit