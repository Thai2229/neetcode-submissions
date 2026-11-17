class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(p1, p2):
            # Base cases
            if p1 == len(word1):
                return len(word2) - p2

            if p2 == len(word2):
                return len(word1) - p1

            # Check memo
            if (p1, p2) in memo:
                return memo[(p1, p2)]

            # Characters match, no operation needed
            if word1[p1] == word2[p2]:
                memo[(p1, p2)] = dfs(p1 + 1, p2 + 1)

            # Characters don't match, try all 3 operations
            else:
                insert = dfs(p1, p2 + 1)
                delete = dfs(p1 + 1, p2)
                replace = dfs(p1 + 1, p2 + 1)

                memo[(p1, p2)] = 1 + min(insert, delete, replace)

            return memo[(p1, p2)]

        return dfs(0, 0)