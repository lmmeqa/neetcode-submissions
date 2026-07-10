class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def getsubset(start, path):
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                getsubset(i+1, path)
                path.pop()
        getsubset(0, [])
        return res