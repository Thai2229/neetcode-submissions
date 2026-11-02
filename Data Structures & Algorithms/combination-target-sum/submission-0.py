class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #good idea to sort so you know when to prune on the backtrack
        nums.sort()

        #logic; since array is sorted, go through all the ways we can create the target
        #starting with nums[i], for example 2, starting with 3 we can go multiple ways and 
        #from there its barbeque chicken
        res = []
        
        def dfs(i, curr_sum, curr_lst):
            if curr_sum > target or i >= len(nums):
                return 
            if curr_sum == target:
                res.append(curr_lst.copy())
                return
            
            #include i again, or move onto the next and don't include
            curr_sum += nums[i]
            curr_lst.append(nums[i])
            dfs(i, curr_sum, curr_lst)

            curr_sum -= nums[i]
            curr_lst.pop()
            dfs(i+1, curr_sum, curr_lst)
        
        dfs(0,0,[])
        
        return res