class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        #use another for loop this is 3 sum
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l, r = j + 1, len(nums) - 1

                #num to check against is nums[i]
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total > target:
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        triplet = sorted([nums[i],nums[j],nums[l],nums[r]])
                        if triplet not in res: res.append(triplet)
                        l += 1
                        r -= 1

                
        
        return res