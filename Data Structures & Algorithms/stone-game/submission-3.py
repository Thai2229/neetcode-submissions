class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #l and r pointers, try to maximize our score (i.e optimal play)
        #return max score values

        memo = {}

        #curr is gonna track current sum 
        def dfs(l,r,curr):
            #base cases
            if (l == r):
                return curr 
            if ((l,r,curr) in memo):
                return memo[(l,r,curr)]


            #take from left or right, return max
            left = dfs(l+1,r,curr+piles[l])
            right = dfs(l,r-1,curr+piles[r])
            
            memo[(l,r,curr)] = max(left,right)
            return memo[(l,r,curr)]




        score = dfs(0,len(piles)-1,0)

        return score > (sum(piles) - score) 





        