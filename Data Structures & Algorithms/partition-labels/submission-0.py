class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #something to do with the last index of a character + hashmap

        seen = {}

        #stores last seen index
        for j in range(len(s)):
            seen[s[j]] = j
        
        res = []
        size = 0
        last_ind = 0

        for i in range(len(s)):
            size += 1
            last_ind = max(last_ind, seen[s[i]])

            if i == last_ind:
                res.append(size)
                size = 0

        return res 
