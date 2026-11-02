# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        recursive DFS
        if not root:
            return 0

        depth = max(self.maxDepth(root.left), self.maxDepth(root.right))
        return 1 + depth
        """
        #iterative bfs
        if not root:
            return 0
        
        q = deque()
        q.append(root)
        level = 0

        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1
        
        return level

        