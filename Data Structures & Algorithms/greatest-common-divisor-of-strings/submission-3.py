class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            res = 0
            while res <= len(str1):
                res += len(str2)

            if len(str1) % (res-len(str1)) == 0:
                if str1[:(res-len(str1))] * (len(str1) // (res-len(str1))) == str1:
                    return str1[:(res-len(str1))]
                else: 
                    return ""
            else:
                return ""
        
        elif len(str1) < len(str2):
            res = 0
            while res <= len(str2):
                res += len(str1)
            
            return str1[:(res-len(str2))]
            if len(str2) % (res-len(str2)) == 0:
                if str1[:(res-len(str2))] * (len(str2) // (res-len(str2))) == str2:
                    return str1[:(res-len(str2))]
                else: 
                    return ""
            else:
                return ""
        else: 
            if str1 == str2: return str1
            return ""