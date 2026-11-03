class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        res = []

        def dfs(index, curr_word):
            if index >= len(digits):
                res.append(curr_word)
                return

            for letter in digit_map[digits[index]]:
                dfs(index + 1, curr_word + letter)

        if not digits:
            return []

        dfs(0, "")
        return res