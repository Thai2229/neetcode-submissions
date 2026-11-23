class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #if any entry in triplet > target, greedily discard it 

        res = [0,0,0]

        for (a,b,c) in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                if a == target[0] or b == target[1] or c == target[2]:
                    res = [max(a,res[0]),max(b,res[1]),max(c,res[2])]

        return res == target 