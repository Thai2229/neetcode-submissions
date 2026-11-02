class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #let dp[i] be the min cost from floor i to get to the end
        #dp[n] = 0 #n is the length of cost
        n = len(cost)
        dp = [0] * (n+2)

        #base case
        dp[n] = 0
        dp[n + 1] = 0 #for ease

        #from n - 1 down to 0
        for i in range(len(cost) - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])
