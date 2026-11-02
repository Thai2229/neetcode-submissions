class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1Freq = {} 
        s2Seen = {}

        if len(s2) < len(s1):
            return False

        for c in s1:
            s1Freq[c] = s1Freq.get(c,0) + 1
        
        for r in range(len(s2)):
            s2Seen[s2[r]] = s2Seen.get(s2[r],0) + 1
            print(s2Seen)
            if r - l + 1 > len(s1):
                s2Seen[s2[l]] -= 1
                l += 1
            
            t,s = 0,0
            for key in s1Freq:
                t += 1
                if s1Freq[key] == s2Seen.get(key,0):
                    s += 1
            if t == s: return True
        
        return False

