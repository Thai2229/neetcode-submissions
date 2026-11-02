class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #two pointers method
        l, r = 0, len(numbers) - 1

        while l < r:
            diff = numbers[r] + numbers[l]
            if diff > target:
                r -= 1
            elif diff < target:
                l += 1
            else:
                return [l+1,r+1]
        
        return []







        #og two sum method
        """
        seen = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in seen:
                return [seen[diff]+1, i+1]
            seen[numbers[i]] = i
        """
        