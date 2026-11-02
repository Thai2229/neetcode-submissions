class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #we need to keep track of the most seen element
        count = {}
        res = 0
        l, r = 0, 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] = count[s[l]] - 1
                l += 1
            res = max(res, r-l+1)
        
        return res