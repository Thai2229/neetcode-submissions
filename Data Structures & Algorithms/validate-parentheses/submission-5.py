class Solution:
    def isValid(self, s: str) -> bool:

        seenStack = []
        
        for bracket in s:
            if bracket in "({[":
                seenStack.append(bracket)
            elif not seenStack:
                return False
            elif bracket == ")" and seenStack[-1] != "(":
                return False
            elif bracket == "]" and seenStack[-1] != "[":
                return False
            elif bracket == "}" and seenStack[-1] != "{":
                return False
            else:
                seenStack.pop()
        
        return len(seenStack) == 0