class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #use a dictionary to store numbers
        #find the minimum number
        numSet = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in numSet:
                count = 1
                for i in range(1,len(nums)):
                    if num + i in numSet:
                        count += 1
                    else: break
                res = max(res,count)
        return res
            

