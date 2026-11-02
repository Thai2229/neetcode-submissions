class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, curr_sum, curr_lst):
            if curr_sum == target:
                res.append(curr_lst.copy())
                return

            if curr_sum > target:
                return

            for i in range(start, len(candidates)):

                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                # Prune: sorted array means remaining numbers are too large
                if curr_sum + candidates[i] > target:
                    break

                curr_lst.append(candidates[i])
                dfs(i + 1, curr_sum + candidates[i], curr_lst)
                curr_lst.pop()

        dfs(0, 0, [])
        return res