class Solution:
    def jump(self, nums: List[int]) -> int:
        #always want to greedily choose the one with the longest reach 

        if len(nums) == 1:
            return 0

        i = 0
        res = 0

        while True:
            res += 1
            reach = i + nums[i]
            #base case
            if reach >= len(nums)-1:
                return res

            best, index = 0, 0
            for j in range(i+1,min(len(nums)-1,reach+1)):
                if j + nums[j] > best:
                    best = j + nums[j]
                    index = j

            i = index             
