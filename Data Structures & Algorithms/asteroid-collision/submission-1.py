class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
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