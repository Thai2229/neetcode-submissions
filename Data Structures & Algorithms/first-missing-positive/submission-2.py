class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1 

        for i in range(1,2^31):
            if i not in seen:
                return i
                