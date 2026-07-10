from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextgreater = defaultdict(lambda:-1)

        for j, num in enumerate(nums2):
            while stack and num>stack[-1]:
                nextgreater[stack.pop()] = num
            stack.append(num)
        res = []
        for num in nums1:
            res.append(nextgreater[num])
        return res

