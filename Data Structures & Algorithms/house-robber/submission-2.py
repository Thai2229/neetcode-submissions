class Solution:
    def rob(self, nums: List[int]) -> int:
        #for the dp recursion, you either choose to rob the house, or you dont
        #base cases
        if len(nums) == 1:
            return nums[0]

        dp = [-1] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        #either choose to rob the house or not
        #so dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[len(nums) - 1]