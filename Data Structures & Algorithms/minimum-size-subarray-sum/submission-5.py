class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        count = 0
        res = sum(nums)

        if res < target:
            return 0

        for r in range(len(nums)):
            count += nums[r]
            
            if count > target:
                while count - nums[l] >= target:
                    count -= nums[l]
                    l += 1

            if count >= target:
                res = min(res, r - l + 1)
        
        return res