class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #use hastable 
        if len(nums) == 0:
            return 0

        seen = {}
        res = 1

        for num in nums:
            if num not in seen:
                seen[num] = 1
        
        for n in nums:
            if (n - 1) in seen:
                continue
            else:
                total = 1
                curr = n + 1
                while curr in seen:
                    total += 1
                    curr += 1
                
                res = max(res,total)
        
        return res