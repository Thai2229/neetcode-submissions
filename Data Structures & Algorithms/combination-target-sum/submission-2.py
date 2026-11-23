class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #choose to include or not include and move onto the next

        #stores 3 things, current sum, current array, current nums index
        
        res = []

        def dfs(index, curr_arr, curr_sum):
            if curr_sum > target:
                return 
            if curr_sum == target:
                res.append(curr_arr)
                return 
            if index > len(nums)-1:
                return 
            
            #include
            dfs(index,curr_arr + [nums[index]],curr_sum + nums[index])

            #exclude 
            dfs(index+1,curr_arr,curr_sum)

        dfs(0,[],0)
        return res