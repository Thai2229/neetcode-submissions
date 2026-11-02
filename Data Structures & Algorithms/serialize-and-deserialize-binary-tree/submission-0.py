from collections import deque

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node is None:
                res.append("null")
                continue

            res.append(str(node.val))

            # Always append both children, even if None
            q.append(node.left)
            q.append(node.right)

        return "#".join(res)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        vals = data.split("#")

        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1

        while q:
            node = q.popleft()

            # Process left child
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1

            # Process right child
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1

        return root