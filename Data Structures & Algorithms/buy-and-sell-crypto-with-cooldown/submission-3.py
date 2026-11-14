class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(index, holding):
            if index >= len(prices):
                return 0

            if (index, holding) in memo:
                return memo[(index, holding)]

            # Option 1: Do nothing
            profit = dfs(index + 1, holding)

            # Option 2: Buy
            if not holding:
                profit = max(
                    profit,
                    -prices[index] + dfs(index + 1, True)
                )

            # Option 3: Sell
            else:
                profit = max(
                    profit,
                    prices[index] + dfs(index + 2, False)
                )

            memo[(index, holding)] = profit
            return profit

        return dfs(0, False)