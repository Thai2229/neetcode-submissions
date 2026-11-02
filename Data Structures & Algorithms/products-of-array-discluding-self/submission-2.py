class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #multiply the entire array, then just divide by the number 

        #edge case, array has only one zero

        total = 1
        total_no_zero = 1
        zero_cnt = 0

        for num in nums:
            if num == 0:
                zero_cnt += 1
                total = total * num 
            else:
                total = total * num 
                total_no_zero = total_no_zero * num
        
        res = [0] * len(nums)
        if zero_cnt == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = total_no_zero
                    return res

        if zero_cnt >= 2:
            return res

        for i in range(len(nums)):
            res[i] = total//nums[i]
        return res

                