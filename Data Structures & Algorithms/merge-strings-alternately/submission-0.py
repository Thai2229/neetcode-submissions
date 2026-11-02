class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = 0
        w2 = 0
        result = ""
        #take the length of the longer word
        while w1 < len(word1) or w2 < len(word2):
            if w1 < len(word1) and w2 < len(word2):
                result = result + word1[w1] + word2[w2]
                w1 += 1
                w2 += 1
            elif w1 < len(word1):
                result = result + word1[w1] 
                w1 += 1
            elif w2 < len(word2):
                result = result + word2[w2]
                w2 += 1

        return result