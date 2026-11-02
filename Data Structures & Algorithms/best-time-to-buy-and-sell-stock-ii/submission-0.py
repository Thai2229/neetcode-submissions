class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #greedy approach
        #why it works example take [1,3,5] buying on day 1, selling on day 2, buying 
        #on day 2, selling on day 3 is the same as buying on day 1 and selling on day 2
        profit = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit