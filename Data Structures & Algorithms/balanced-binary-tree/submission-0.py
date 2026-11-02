# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #call dfs, if height.dfs.left - height.dfs.right > 1: return false
        Flag = True
        def dfs(curr):
            nonlocal Flag
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
 
            if abs(left-right) > 1:
                Flag = False
            return 1 + max(left,right)

        dfs(root)
        return Flag