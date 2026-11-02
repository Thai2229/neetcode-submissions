class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #you will need to do n/2 total operations, this fixes
        #both the odd and even problem
        left = 0
        right = len(s) - 1
        for i in range(len(s) // 2):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            
            left += 1
            right -= 1
