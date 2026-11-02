class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2 
            if nums[mid] == target:
                return mid

            #we are in the left sorted portion
            if nums[l] <= nums[mid]:
                #move to the right sorted portion if conditions met
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            #in right sorted portion
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1