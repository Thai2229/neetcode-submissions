class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}

        # dfs returns max coins possible from remaining balloons
        def dfs(nums):
            if len(nums) == 0:
                return 0

            key = tuple(nums)

            if key in memo:
                return memo[key]

            best = 0

            for i in range(len(nums)):
                # Find neighboring balloons
                left = nums[i - 1] if i > 0 else 1
                right = nums[i + 1] if i < len(nums) - 1 else 1

                # Coins gained by bursting balloon i
                total = left * nums[i] * right

                # Remove balloon i without modifying original list
                remaining = nums[:i] + nums[i + 1:]

                # Try bursting this balloon, then solve remainder
                best = max(best, total + dfs(remaining))

            memo[key] = best
            return best

        return dfs(nums)