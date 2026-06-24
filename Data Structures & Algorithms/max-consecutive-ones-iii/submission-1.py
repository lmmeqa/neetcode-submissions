class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        seencount = 0
        left = 0
        result = 0
        for right in range(0,len(nums)):
            if nums[right] == 0:
                seencount+=1
            while seencount > k:
                if nums[left] == 0:
                    seencount-=1
                left+=1 
            result = max(result, right - left + 1)
        return result
            