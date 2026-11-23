class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #decide to either include or exclude each number

        res = []

        #keep track of index and current array 
        def dfs(index, curr):
            if index >= len(nums):
                res.append(curr)
                return 
            
            #include
            dfs(index+1,curr + [nums[index]])

            #exclude
            dfs(index+1,curr)


        dfs(0,[])
        return res  