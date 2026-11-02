class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #let dp[i][j] be the number of paths from (i,j)
        #to (m - 1, n - 1)

        dp = [[0] * (n) for _ in range(m)]

        #base case
        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m - 1 and j == n - 1: continue
                right = dp[i][j+1] if j + 1 < n else 0
                down = dp[i+1][j] if i + 1 < m else 0

                dp[i][j] = right + down

        #dp[i][j] = dp[i][j+1] + dp[i+1][j]
        #given that j+1 and i+1 are valid

        
        return dp[0][0]