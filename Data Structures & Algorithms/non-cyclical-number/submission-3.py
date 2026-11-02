class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}

        while True:
            res = 0
            for digit in str(n):
                res += (int(digit) * int(digit))
            
            n = res
            if res in seen:
                break
            else: 
                seen[res] = 1
        return n == 1