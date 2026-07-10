class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, allnums):
            res.append(allnums[:])
            for i in range(start, len(nums)):
                allnums.append(nums[i])
                backtrack(i+1, allnums)
                allnums.pop()
        backtrack(0,[])
        return res