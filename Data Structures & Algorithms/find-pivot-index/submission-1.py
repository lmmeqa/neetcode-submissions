class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        rightsum = sum(nums) - nums[0]
        leftsum = 0
        pivot = 0
        while pivot < len(nums):
            if leftsum == rightsum:
                return pivot
            leftsum+=nums[pivot]
            pivot+=1
            if not pivot<len(nums): return -1
            rightsum-=nums[pivot]
        return -1

        
