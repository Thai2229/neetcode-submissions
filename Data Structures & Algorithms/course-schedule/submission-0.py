class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # 0 = unvisited, 1 = currently visiting, 2 = fully visited
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False  # Cycle detected

            if state[course] == 2:
                return True  # Already checked, no cycle

            state[course] = 1

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False

        return True