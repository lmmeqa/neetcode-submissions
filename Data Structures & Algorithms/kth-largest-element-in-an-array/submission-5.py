import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k + 1
        heapq.heapify(nums)
        current = None
        while k:
            current = heapq.heappop(nums)
            k-=1
        return current