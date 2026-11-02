class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for ind, num in enumerate(nums):
            seen[num] = ind
        
        for ind, num in enumerate(nums):
            diff = target - num 
            if diff in seen and ind != seen[diff]:
                return [ind, seen[diff]]