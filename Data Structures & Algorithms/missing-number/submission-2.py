class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums):
            if index == nums[index]:
                index+=1
            else:
                if nums[index]==len(nums):
                    index+=1
                    continue
                temp = nums[nums[index]]
                nums[nums[index]] = nums[index]
                nums[index] = temp
        for index, num in enumerate(nums):
            if index!=num:
                return index
        return len(nums)
            

