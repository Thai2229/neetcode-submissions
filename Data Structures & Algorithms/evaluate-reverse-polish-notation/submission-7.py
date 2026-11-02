class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #store numbers in stack, if you see any operator
        #pop from stack twice, do operator on both numbers, append back to stack

        stack = []

        for token in tokens:
            if token == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1+num2)
            elif token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2-num1)
            elif token == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)
            elif token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2/num1))
            else:
                stack.append(int(token))
        
        return stack[-1]