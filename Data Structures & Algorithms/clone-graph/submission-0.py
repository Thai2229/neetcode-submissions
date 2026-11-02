
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # key: original node, value: cloned node
        seen = {}
        q = deque()
        q.append(node)
        seen[node] = Node(node.val)

        while q:
            curr = q.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in seen:
                    seen[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                # Connect the cloned node to the cloned neighbor
                seen[curr].neighbors.append(seen[neighbor])

        return seen[node]
