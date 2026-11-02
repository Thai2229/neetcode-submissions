class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            volume = min(heights[l], heights[r]) * (r-l)
            res = max(res,volume)
            
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return res