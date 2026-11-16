class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #key intuition, choose either the character from a or the 
        #character from b 

        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        #p1 goes to s1, p2 goes to s2
        
        def dfs(p1, p2):
            if p1 == len(s1) and p2 == len(s2):
                return True
            if (p1, p2) in memo:
                return memo[(p1, p2)]

            memo[(p1, p2)] = False

            if p1 < len(s1) and s1[p1] == s3[p1 + p2] and dfs(p1 + 1, p2):
                memo[(p1, p2)] = True
            elif p2 < len(s2) and s2[p2] == s3[p1 + p2] and dfs(p1, p2 + 1):
                memo[(p1, p2)] = True

            return memo[(p1, p2)]

        return dfs(0, 0)