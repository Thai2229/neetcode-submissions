class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False 
        
        s1cnt = {}
        for i in range(len(s1)):
            s1cnt[s1[i]] = s1cnt.get(s1[i], 0) + 1

        l, r = 0, len(s1)-1    
        s2cnt = {}
        for j in range(l,r+1):
            s2cnt[s2[j]] = s2cnt.get(s2[j], 0) + 1

        while r < len(s2):
            if s2cnt == s1cnt: 
                return True

            s2cnt[s2[l]] -= 1
            if s2cnt[s2[l]] == 0:
                del s2cnt[s2[l]]
            l += 1
            r += 1
            if r < len(s2):
                s2cnt[s2[r]] = s2cnt.get(s2[r], 0) + 1
        
        return False