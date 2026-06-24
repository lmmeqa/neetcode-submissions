class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occurrence = nums.count(val)
        k = len(nums) - occurrence
        replacements = []
        for i in nums[k:]:
            if i != val:
                replacements.append(i)
        replacement_id = 0
        for i in range(0,k):
            if nums[i] == val:
                nums[i] = replacements[replacement_id]
                replacement_id+=1
        nums[k:] = [val]*k
        return k
        