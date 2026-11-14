class Solution:
    def countBits(self, n: int) -> List[int]:
        #use a bitmask and, for each number 0 through n
        #and it with n itself (the bitmask)

        res = []
        for i in range(n + 1):
            count = 0
            num = i

            while num > 0:
                count += num & 1
                num >>= 1

            res.append(count)
        return res