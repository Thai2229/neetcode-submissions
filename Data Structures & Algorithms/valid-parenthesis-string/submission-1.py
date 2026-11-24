class Solution:
    def checkValidString(self, s: str) -> bool:
        #use a stack to track left parenthesis "("
        #keep a running count of * seen? 
        #use it to greedily match "("
        
        #important case ()*)
        #fails on *(
        #need to keep track of position 

        stack = []
        stars = []

        for i in range(len(s)):
            char = s[i]
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            else:
                stars.append(i)

        while stack and stars:
            if stack[-1] < stars[-1]:
                stack.pop()
                stars.pop()
            else:
                return False

        return not stack


        



