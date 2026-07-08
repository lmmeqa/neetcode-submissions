class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid]<target:
                lo = mid+1
            else:
                hi = mid
        if nums[lo] >= target:
            return lo
        else:
            return lo + 1
            
        