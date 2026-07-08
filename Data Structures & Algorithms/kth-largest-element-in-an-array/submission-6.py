import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numsheap = []
        for num in nums:
            heapq.heappush(numsheap,num)
            if len(numsheap) > k:
                heapq.heappop(numsheap)
        return heapq.heappop(numsheap)