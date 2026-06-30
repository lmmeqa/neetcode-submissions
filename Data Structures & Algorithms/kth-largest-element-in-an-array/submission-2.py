class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxnum = max(max(nums), abs(min(nums)))
        counts = [0]*(maxnum*2 + 1)
        for num in nums:
            counts[num+maxnum]+=1
        for i in range(len(counts)-1, -1, -1):
            k-=counts[i]
            if k <= 0:
                return i-maxnum