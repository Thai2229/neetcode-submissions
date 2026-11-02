# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #where the split occurs is the lowest common ancestor
        #edge case, if curr == p.val or q.val return curr

        curr = root
        while curr:
            if curr.val == p.val or curr.val == q.val:
                return curr
            if curr.val > p.val and curr.val < q.val:
                return curr
            if curr.val < p.val and curr.val > q.val:
                return curr
            if p.val > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        
