class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        res = 0
        charSet = set(s)

        for c in charSet:
            l = 0
            count = 0
            diffCount = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                else: 
                    diffCount += 1
                
                while diffCount > k:
                    if s[l] != c:
                        diffCount -= 1
                    l += 1

                res = max(res, r - l + 1)

            

        return res