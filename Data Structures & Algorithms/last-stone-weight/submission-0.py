import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneheap = []
        for stone in stones:
            heapq.heappush(stoneheap, -1*stone)
        while len(stoneheap) > 1:
            largest = -heapq.heappop(stoneheap)
            second = -heapq.heappop(stoneheap)
            if largest > second: heapq.heappush(stoneheap, second - largest)
        return 0 if not stoneheap else -stoneheap[0]
        

        