class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)

        # Build adjacency list
        for src, dst in tickets:
            adj[src].append(dst)

        # Reverse sort so pop() gets the alphabetically smallest airport
        for src in adj:
            adj[src].sort(reverse=True)

        res = []

        def dfs(airport):
            while adj[airport]:
                next_airport = adj[airport].pop()
                dfs(next_airport)

            # Add airport after using all its outgoing tickets
            res.append(airport)

        dfs("JFK")

        # Reverse because airports were added during backtracking
        return res[::-1]