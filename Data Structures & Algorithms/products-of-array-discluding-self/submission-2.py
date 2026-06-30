class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        maxnum = max(max(nums), abs(min(nums)))
        counts = [0]* (maxnum*2 + 1)
        res = [1]*len(nums)
        for num in nums:
            counts[num+maxnum]+=1
        
        for index, num in enumerate(nums):
            countscopy = counts[:]
            countscopy[num+maxnum]-=1
            for indexcount, count in enumerate(countscopy):
                res[index] *= (indexcount-maxnum) ** count
        return res

            