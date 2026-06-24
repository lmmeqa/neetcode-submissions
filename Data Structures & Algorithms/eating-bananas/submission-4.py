import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def caneat(speed:int):
            hours = 0
            for pile in piles:
                hours+=math.ceil(pile/speed)
            if hours>h:
                return False
            return True

        low = 1
        high = max(piles)

        while low!=high:
            mid = (high+low)//2
            if caneat(mid):
                high = mid
            else:
                low = mid + 1

        return low

            
        
            

        
            


