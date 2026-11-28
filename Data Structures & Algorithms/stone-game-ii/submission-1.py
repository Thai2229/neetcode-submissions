class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        #dp problem with top down


        memo = {}

        #track index
        def dfs(i, m):
            total = sum(piles[i:])
            best = 0

            #base cases
            if (i + 2*m >= len(piles)):
                return total 
            if (i,m) in memo:
                return memo[(i,m)]

            #recursion logic
            for x in range(1, min(2 * m, len(piles) - i) + 1):
                bob_score = dfs(i + x, max(m, x))
                potential = total - bob_score 
                best = max(best,potential)
    
            memo[(i,m)] = best
            return best

        return dfs(0,1)