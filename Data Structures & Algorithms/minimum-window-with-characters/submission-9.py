class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = ""
        seen = {}
        target = {}

        #build target count
        for c in t:
            target[c] = target.get(c,0) + 1

        have = 0
        need = len(target)
        
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r],0) + 1
            #update have 
            if s[r] in target and seen[s[r]] == target[s[r]]:
                have += 1

            while have == need:
                temp = s[l:r+1]
                if not res or len(temp) < len(res):
                    res = temp
                
                seen[s[l]] -= 1
                if s[l] in target and seen[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
            
        return res

        """
        helper function too inefficient, instead we use have and need
        def contains():
            for char in target:
                if seen.get(char,0) < target[char]:
                    return False
            return True

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r],0) + 1

            while contains():
                temp = s[l:r+1]

                #not res checks if res = "" ie we havent recorded solution yet
                if not res or len(temp) < len(res): 
                    res = temp
                
                seen[s[l]] -= 1
                l += 1
        """




        