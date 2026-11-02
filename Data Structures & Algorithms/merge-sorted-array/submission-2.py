class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #three pointer solution, one points to a copy of nums1, one points to nums2
        #one points to the real nums1, compare both pointers and input the less
        #than one
        
        #basic algo: put num2 in last nums1 slot then sort:
        #nums1[m:] = nums2[:n], nums1.sort()

        nums1Copy = nums1[:m]
        p1, p2 = 0, 0

        for i in range(m + n):
            if p1 >= m:
                nums1[i] = nums2[p2]
                p2 += 1
            elif p2 >= n:
                nums1[i] = nums1Copy[p1]
                p1 += 1
            elif nums1Copy[p1] <= nums2[p2]:
                nums1[i] = nums1Copy[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1


        