class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = {}
        prefixSum[0] = 1
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            if (curr_sum - k) in prefixSum:
                res += prefixSum[(curr_sum - k)]
            
            if curr_sum in prefixSum:
                prefixSum[curr_sum] += 1
            else: 
                prefixSum[curr_sum] = 1
            
            
        return res
            


