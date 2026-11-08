class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False

        target = target // 2

        memo = {}

        def dfs(curr_index, target):
            if target == 0:
                return True

            if curr_index >= len(nums) or target < 0:
                return False

            # check if we've already calculated this state
            if (curr_index, target) in memo:
                return memo[(curr_index, target)]

            # include
            include = dfs(curr_index + 1, target - nums[curr_index])

            # exclude
            exclude = dfs(curr_index + 1, target)

            memo[(curr_index, target)] = include or exclude

            return memo[(curr_index, target)]

        return dfs(0, target)