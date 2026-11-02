class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #use binary search, find the mid point, expand out from there
        def insert(arr,x):
            l, r = 0, len(arr) - 1

            while l <= r:
                m = (l + r) // 2

                if arr[m] > x:
                    r = m - 1
                elif arr[m] < x:
                    l = m + 1
                else:
                    return m
            
            return l
        
        right = insert(arr,x)
        left = right - 1
        res = []

        while len(res) < k:
            if left >= 0 and right < len(arr):
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    res.append(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
            elif right < len(arr):
                res.append(arr[right])
                right += 1
            else:
                res.append(arr[left])
                left -= 1







        return sorted(res)