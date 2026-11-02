class Solution:
    def isPalindrome(self, s: str) -> bool:
        holder = ""
        for char in s:
            if char.isalnum():
                holder = holder + char.lower()

        l, r = 0, len(holder) - 1

        while l < r:
            if holder[l] != holder[r]:
                return False
            l += 1
            r -= 1
        return True