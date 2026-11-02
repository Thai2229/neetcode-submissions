class Solution:
    def mySqrt(self, x: int) -> int:
        #bounds of square root: 1 to x
        l, r = 1, x
        res = 0

        while l <= r:
            m = (l + r) // 2

            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
                res = max(res,m)
            else:
                return m
        return res