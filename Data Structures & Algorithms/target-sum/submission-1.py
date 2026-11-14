class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #intuition: choose to either make the number negative or positive
        #gonna build top down with dfs 
        memo = {}

        def dfs(index,curr_sum):
            #return if the index >= nums, return 1 if sum = target
            if index >= len(nums):
                return 1 if curr_sum == target else 0
            if (index, curr_sum) in memo:
                return memo[(index,curr_sum)]

            ways = 0
            #choosing subtraction
            ways += dfs(index+1,curr_sum-nums[index])
            #choosing to add 
            ways += dfs(index+1,curr_sum+nums[index])

            memo[(index,curr_sum)] = ways 


            return ways 
            


        return dfs(0,0)
