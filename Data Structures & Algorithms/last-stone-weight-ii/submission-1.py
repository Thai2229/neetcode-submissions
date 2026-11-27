class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        memo = {}

        def dfs(curr, curr_sum):
            if curr >= len(stones):
                return curr_sum

            if curr_sum == target:
                return curr_sum

            if (curr, curr_sum) in memo:
                return memo[(curr,curr_sum)]


            exclude = dfs(curr + 1, curr_sum)
            memo[(curr+1,curr_sum)] = exclude

            include = 0
            if curr_sum + stones[curr] <= target:
                include = dfs(curr + 1, curr_sum + stones[curr])
                memo[(curr+1,curr_sum + stones[curr])] = include

            return max(exclude, include)

        return total - 2 * dfs(0, 0)