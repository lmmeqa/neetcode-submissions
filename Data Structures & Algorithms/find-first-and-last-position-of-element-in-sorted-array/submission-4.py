class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums) - 1
        ## find lower bound
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        lowbound = lo
        
        if not nums or nums[lowbound] != target: return [-1,-1]

        lo = lowbound
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi + 1)//2
            if nums[mid] <= target:
                lo = mid
            else:
                hi = mid - 1
        
        return [-1,-1] if lowbound < 0 or hi < 0 else [lowbound, hi]

        