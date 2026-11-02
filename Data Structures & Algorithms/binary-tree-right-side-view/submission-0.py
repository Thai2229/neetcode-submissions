# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS traverse level by level, then return the rightmost on each level
        if not root:
            return []

        levels = []
        q = deque()
        q.append(root)
        
        while q:
            size = len(q)
            level = []

            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                level.append(node.val)

            levels.append(level)
        
        res = []
        for l in levels:
            res.append(l[-1])
        return res
