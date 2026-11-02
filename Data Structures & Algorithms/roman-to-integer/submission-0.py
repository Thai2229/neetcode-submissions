class Solution:
    def romanToInt(self, s: str) -> int:
        num_conv = {"I": 1, "V": 5, "X": 10, "L": 50, "C" : 100, "D": 500, "M": 1000}
        right = 0
        res = 0
        
        while right < len(s):
            char = s[right]
            Next = right + 1
            
            if char == "I" and Next < len(s) and (s[Next] == "V" or s[Next] == "X"):
                res += (num_conv[s[Next]] - 1)
                right += 2
            elif char == "X" and Next < len(s) and (s[Next] == "L" or s[Next] == "C"):
                res += (num_conv[s[Next]] - 10)
                right += 2
            elif char == "C" and Next < len(s) and (s[Next] == "D" or s[Next] == "M"):
                res += (num_conv[s[Next]] - 100)
                right += 2
            else:
                res += num_conv[char]
                right += 1
        
        
        return res