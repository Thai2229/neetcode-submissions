class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            #num to check against is nums[i]
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    triplet = sorted([nums[i],nums[l],nums[r]])
                    if triplet not in res: res.append(triplet)
                    l += 1
                    r -= 1

                
        
        return res
