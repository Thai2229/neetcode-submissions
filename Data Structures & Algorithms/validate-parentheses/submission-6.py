class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if p_map[char] != top:
                    return False
        
        return len(stack) == 0