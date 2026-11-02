class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #just add to a stack, if the current sign is different from the top of the stack
        #then compare and see if they destroy
        
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack

