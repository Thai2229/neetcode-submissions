import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #use binary search to determine the bannans per hour of eating
        #the minimum is 1 and the max is the max of piles
        #example : piles is [1, 25, 23], use binary search to determine
        #between 1 and 25

        #basically use binary search narrow down between max or the piles 
        #and 1, then gonna have to loop through piles to see if mid works or if it 
        #does

        #determines if you can eat all bannannas with h hours with m eating rate
        res = 1

        def bannana(m):
            hours = 0
            for b in piles:
                hours += math.ceil(b / m)
            if hours > h:
                return False
            return True
            

        max_piles = piles[0]
        for b in piles:
            max_piles = max(max_piles, b)
        
        l, r = 1, max_piles
        while l < r:
            mid = l + (r-l)//2
            if bannana(mid):
                r = mid
            else:
                l = mid + 1
        
        return r








        return res 