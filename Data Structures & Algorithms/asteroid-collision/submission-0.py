class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Iterate through the list
        # If the element is positive, push to the stack
        # If the element is negative, compare the size (abs) to the top of the stack (peek)
        # If the elements are the same size, pop from the stack
        # If the top of the stack is greater, nothing happens, continue
        # If the top of the stack is smaller, pop from the stack until an asterioid with a greater size is there
        # If there is no asteroid with a greater size, push the negative asterioid at the end
        # Return the stack

        mag = []

        for ast in asteroids:
            alive = True
            
            while alive and ast < 0 and mag and mag[-1] > 0:
                if mag[-1] < -ast:
                    mag.pop()
                elif mag[-1] == -ast:
                    mag.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                mag.append(ast)

        return mag