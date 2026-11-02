class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #edge case: zero at one point
        #if its zero at two points or more entire array is 0

        product = 1
        seen_zero = False
        zero_loc = None

        for i in range(len(nums)):
            if nums[i] == 0 and seen_zero:
                return [0] * len(nums)
            elif nums[i] == 0:
                seen_zero = True
                zero_loc = i
                continue 
            else:
                product = product * nums[i]
        
        res = [0] * len(nums)
        
        if seen_zero:
            res[zero_loc] = product
            return res
        
        for j in range(len(nums)):
            res[j] = product // nums[j]
        
        return res
