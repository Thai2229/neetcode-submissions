class Solution:
    def encode(self, strs: List[str]) -> str:

        #  4#funs5#dudee#6heyyyy

        res = ""

        for s in strs: 
            s_encode = str(len(s)) + "#" + s
            res = res + s_encode

        return res


    def decode(self, s: str) -> List[str]:
        p = 0
        res = []

        while p < len(s):
            word = ""
            length = ""

            while s[p] != "#":
                length = length + s[p]
                p += 1
            
            length = int(length)
            p += 1

            for i in range(p, p + length):
                word = word + s[i]
            
            res.append(word)
            p = p + length

        return res


