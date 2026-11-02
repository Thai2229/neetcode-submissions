class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #go with approach check one character at a time
        #solution, think of using two for loops: store the character in the first 
        #word to compare, then keep incrementing it and compare it again all the 
        #other characters
        prefix = ""
        for i in range (len(strs[0])):
            char = strs[0][i]
            for word in strs: #definitely the right path consider indexing
                if i >= len(word): return prefix
                if char != word[i]: return prefix
            prefix = prefix + char
        return prefix