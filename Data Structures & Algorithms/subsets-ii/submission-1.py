class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(index, curr_subset):
            # Every current subset is a valid answer
            res.append(curr_subset.copy())

            for i in range(index, len(nums)):
                # Skip duplicates at the same recursion level
                if i > index and nums[i] == nums[i - 1]:
                    continue

                # Include current number
                curr_subset.append(nums[i])

                # Recurse to build the next subset
                dfs(i + 1, curr_subset)

                # Backtrack
                curr_subset.pop()

        dfs(0, [])
        return res