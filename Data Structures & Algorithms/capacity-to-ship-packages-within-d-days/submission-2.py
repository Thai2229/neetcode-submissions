class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #weight range: max of array -> sum of array 

        sum_w = 0
        max_w = 0

        for i in range(len(weights)):
            weight = weights[i]
            sum_w += weight
            max_w = max(max_w,weight)

        def test(weight):
            curr = 0 
            num_days = 1

            for i in range(len(weights)):
                if curr + weights[i] > weight:
                    num_days += 1
                    curr = 0
                    
                curr += weights[i]

            return num_days <= days

        #binary search on max of array -> sum of array and test if it will work 
        l, r = max_w, sum_w

        while l < r:
            mid = (l+r) // 2
            if test(mid):
                r = mid 
            else:
                l = mid + 1
        
        return l






