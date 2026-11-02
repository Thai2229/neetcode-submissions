class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #intuition, stack is going to be sorted in descending order
        #if you encounter a number greater than the top of the stack, pop it off,
        #store the index

        #store in stack a tuple? its temp and index?
        #stack = [temp,index]

        stack = []
        res = len(temperatures) * [0]

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temp > stack[-1][0]:
                popped = stack.pop()
                res[popped[1]] = i - popped[1]
            stack.append((temp,i))
        
        return res
