class Solution:
    def trap(self, height: List[int]) -> int:
        #how to calculate water at each position: 
        #the minimum of left and right minus the height of the position
        #in code: min(l,r) - height[i]
        #then for each position we need to figure out its max left and right height

        left, right = 0, len(height)-1
        maxRight = [0] * len(height)
        maxLeft = [0] * len(height)
        currLeftMax, currRightMax = height[0], height[len(height)-1]

        for l in range(1, len(height)):
            maxLeft[l] = currLeftMax
            currLeftMax = max(currLeftMax, height[l])
        
        for r in range(len(height)-2,-1,-1):
            maxRight[r] = currRightMax
            currRightMax = max(currRightMax, height[r])

        res = 0
        for i in range(len(height)):
            res = res + max(0,min(maxLeft[i],maxRight[i]) - height[i])

        return res