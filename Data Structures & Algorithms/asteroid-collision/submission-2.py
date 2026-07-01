class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        index = 0
        while index < len(asteroids)-1:
            if asteroids[index] >0 and asteroids[index + 1] < 0:
                if abs(asteroids[index]) > abs(asteroids[index + 1]):
                    asteroids.pop(index+1)
                elif abs(asteroids[index]) < abs(asteroids[index + 1]):
                    asteroids.pop(index)
                    index = max(0,index-1)
                else:
                    asteroids.pop(index + 1)
                    asteroids.pop(index)
                    index = max(0,index-1)
            else:
                index+=1
        return asteroids


            