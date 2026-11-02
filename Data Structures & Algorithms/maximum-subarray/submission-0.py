class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr = nums[0], 0

        for num in nums:
            if curr + num > num:
                curr = curr + num
            else: 
                curr = num
            res = max(res,curr)

        return res

