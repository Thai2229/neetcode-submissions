class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(curr, max_seen):
            nonlocal res

            if not curr:
                return

            if curr.val >= max_seen:
                res += 1

            max_seen = max(max_seen, curr.val)

            dfs(curr.left, max_seen)
            dfs(curr.right, max_seen)

        dfs(root, root.val)
        return res