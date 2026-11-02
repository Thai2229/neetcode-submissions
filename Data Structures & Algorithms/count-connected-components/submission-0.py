class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #run dfs, while len(visited) < n, increment result by 1 everytime
        #you start a completely new dfs
        adj = {i:[] for i in range(n)}
        visited = set()

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
        
        return res