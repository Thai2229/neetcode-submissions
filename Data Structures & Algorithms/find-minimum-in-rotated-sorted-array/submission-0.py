class Solution:
    def findMin(self, nums: List[int]) -> int:
        #solution find the pivot
        #imagine the array 3, 4, 5, 1, 2
        #l = 3, r = 2, mid = 5
        #if nums[r] > nums[mid]
        #you can discard the entire right side since you know its sorted correct
        # 1, 2, 3, 4, 5
        l, r = 0, len(nums)-1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = l + (r-l)//2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid
        
        return res