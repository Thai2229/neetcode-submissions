class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #choose whether to include or not include, should include
        #when s[index] == t[curr]
        #curr keeps track of the index of t we are on

        #lets say i have s = caaat 
        #t = cat 
        #dfs: choose (c)aaat
        #subproblem: how many ways can cat be formed from choosing 
        #that c at the start? 

        #base cases either curr == len(t) return 1or index >= len(s) return 0

        memo = {}

        def dfs(index, curr):
            if (index,curr) in memo:
                return memo[index,curr]
            if curr == len(t):
                return 1
            if index >= len(s): 
                return 0 
            
            #can choose to skip or can choose the letter if s[index] == t[curr]
            best = 0
            best += dfs(index+1, curr)
            if s[index] == t[curr]:
                best += dfs(index+1, curr+1)
            
            memo[(index,curr)] = best
            return best



        return dfs(0,0) 