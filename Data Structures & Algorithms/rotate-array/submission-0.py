class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy = [0] * len(nums)
        for i in range(len(nums)):
            copy[(i + k) % len(nums)] = nums[i]

        for j in range(len(nums)):
            nums[j] = copy[j]