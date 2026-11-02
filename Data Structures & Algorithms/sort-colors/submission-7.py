class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #intuition, you know that 0 can always go at the beginning and 2 can
        #always go at the end, so just put 1 in the middle
        
        zero, one, two = 0, 0, 0
        res = []

        for num in nums:
            if num == 0:
                zero += 1
            elif num == 1:
                one += 1
            else:
                two += 1
        
        res = [0] * zero + [1] * one + [2] * two
        for i in range(len(nums)):
            nums[i] = res[i]
        
        
