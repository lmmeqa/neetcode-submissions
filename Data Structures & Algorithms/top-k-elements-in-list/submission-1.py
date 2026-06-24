from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i]+=1
        res = []
        for value in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:k]:
            res.append(value[0])
        return res

              
        