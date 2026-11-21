class Solution:
    def jump(self, nums: List[int]) -> int:
        #? greadily choose the biggest number in reach

        index = 0
        res = 0
        
        while index < len(nums)-1:
            res += 1
            reach = index + nums[index]
            if reach >= len(nums)-1:
                return res
            
            curr_max = reach 
            for i in range(index+1,reach+1):
                if i+nums[i] > curr_max:
                    index = i
                    curr_max = i + nums[i]

        return res