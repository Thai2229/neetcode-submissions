class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(0,len(temperatures)):
            while stack:
                if temperatures[i] > temperatures[stack[-1]]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
                else:
                    break
            stack.append(i)
        
        while stack:
            res[stack[-1]] = 0
            stack.pop()
        
        return res