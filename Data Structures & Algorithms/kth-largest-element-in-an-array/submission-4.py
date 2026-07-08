import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for index,num in enumerate(nums):
            nums[index] = -num
        heapq.heapify(nums)
        current = None
        while k:
            current = heapq.heappop(nums)
            k-=1
        return -current