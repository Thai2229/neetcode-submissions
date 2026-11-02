class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        found = set()

        for i in range(len(nums)):
            target = -nums[i]
            seen = {}

            for j in range(i + 1, len(nums)):
                seen[nums[j]] = j

            for z in range(i + 1, len(nums)):
                diff = target - nums[z]

                if diff in seen and z != seen[diff]:
                    triplet = tuple(sorted([nums[i], nums[z], diff]))

                    if triplet not in found:
                        found.add(triplet)
                        res.append(list(triplet))

        return res