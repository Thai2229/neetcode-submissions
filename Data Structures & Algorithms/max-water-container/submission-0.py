class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        volume = (right - left) * min(heights[left],heights[right])
        while left != right:
            if heights[left] < heights[right]:
                left += 1
            else: right -= 1
            volume = max(volume,(right - left) * min(heights[left],heights[right]))

        return volume
