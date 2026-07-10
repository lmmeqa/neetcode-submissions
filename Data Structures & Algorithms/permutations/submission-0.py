class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recurse(remaining, curr):
            if not remaining:
                res.append(curr[:])
                return
            for num in remaining:
                curr.append(num)
                newremaining = remaining[:]
                newremaining.remove(num)
                recurse(newremaining, curr)
                curr.pop()
        recurse(nums,[])
        return res



        

