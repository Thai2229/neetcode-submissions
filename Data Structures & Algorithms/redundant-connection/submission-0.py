class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for u, v in edges:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)
            adj[v].append(u)

        potential = set()

        def dfs(node, parent, visited):
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue

                if nei in visited:
                    potential.add(tuple(sorted([node, nei])))
                    continue

                dfs(nei, node, visited)

        for node in adj:
            dfs(node, -1, set())

        for u, v in reversed(edges):
            if tuple(sorted([u, v])) in potential:
                return [u, v]