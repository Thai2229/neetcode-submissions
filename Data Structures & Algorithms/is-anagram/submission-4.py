class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        if len(s) != len(t): 
            return False
        
        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i],0) + 1
            t_count[t[i]] = t_count.get(t[i],0) + 1
        
        for key in s_count:
            if key not in t_count:
                return False
            elif s_count[key] != t_count[key]:
                return False
        
        return True