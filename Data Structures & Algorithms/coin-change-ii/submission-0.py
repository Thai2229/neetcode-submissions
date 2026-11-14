class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #lets go bottom up dp, dp needs to be of length amount+1
        dp = [0]*(amount+1)
        dp[0] = 1

        #what is the dp relation?
        #dp[i] = dp[i] + dp[i-coin]
        for coin in coins:
            for i in range(1, len(dp)):
                if i >= coin:
                    dp[i] = dp[i] + dp[i-coin]
        
        return dp[amount]