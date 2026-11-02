class Solution:
    def trap(self, height: List[int]) -> int:
        #key intuition, you scan through the array and calculate the water
        #at each position i
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0 #start using this for solution

        #you want to move left or right and keep the highest known position
        while l < r:
            if leftMax < rightMax:
                res += leftMax - height[l]
                l += 1
                leftMax = max(leftMax, height[l])
            else:
                res += rightMax - height[r]
                r -= 1
                rightMax = max(rightMax, height[r])

        
        return res



