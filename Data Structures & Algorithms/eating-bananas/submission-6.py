class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(k):
            hours = 0
            for pile in piles:
                hours+=-1*(pile//(-1*k))
            return hours<=h
        
        hi = max(piles)
        lo = 1
        while lo < hi:
            mid = (lo + hi)//2
            if feasible(mid):
                hi = mid
            else:
                lo = mid+1
        return lo