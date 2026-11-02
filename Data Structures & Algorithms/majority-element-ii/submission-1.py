class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = {}
        res = []

        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1
        
        for num in seen.keys():
            if seen[num] > n/3:
                res.append(num)

        
        return res