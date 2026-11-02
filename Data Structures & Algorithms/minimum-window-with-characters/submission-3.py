class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = 0

        window = {}
        target = {}

        for char in t:
            target[char] = target.get(char, 0) + 1

        have = 0
        need = len(target)

        for r in range(len(s)):
            right = s[r]
            window[right] = window.get(right, 0) + 1

            if right in target and window[right] == target[right]:
                have += 1

            while have == need:
                if res == "" or (r - l + 1) < len(res):
                    res = s[l:r+1]

                left = s[l]
                window[left] -= 1

                if left in target and window[left] < target[left]:
                    have -= 1

                l += 1

        return res