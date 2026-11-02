# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #when you create a path from the root, it splits into two subtrees, the left and right
        #so you want to do root + max_path(left.subtree) + max_path(right.subtree)
        #you want to process max_path of left and right first so you're going to use
        #post order dfs, i.e left, right, root
        #edge case, choose to not include value if negative
        res = root.val

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax,0) #choose to include or not
            rightMax = max(rightMax,0)

            res = max(res, node.val + leftMax + rightMax)

            return node.val + max(leftMax,rightMax) #you can only take one path
        
        dfs(root)
        return res

        