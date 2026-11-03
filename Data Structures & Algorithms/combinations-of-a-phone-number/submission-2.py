class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #first create a mapping of digits in a dictionary to map numbers to the thing
        
        #just pass in index
        #core logic: run dfs on each digit, when you reach the "end" i.e. the length of the 
        #current word is greater than or equal to digits, add it res and return
        #then run a for loop on all the possible letters mapped to each number and call dfs on that
        #popping after each one
        digit_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8":  "tuv", "9": "wxyz"}
        res = []

        def dfs(index, curr_word):
            if index >= len(digits):
                res.append(curr_word)
                return 
            
            for letter in digit_map[digits[index]]:
                dfs(index+1, curr_word + letter)

        if not digits:
            return []

        dfs(0,"")
        return res