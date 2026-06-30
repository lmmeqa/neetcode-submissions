from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        difference = defaultdict(lambda: None)
        for index, num in enumerate(numbers):
            if difference[num] != None:
                return [index + 1, difference[num] + 1] if index+1 < difference[num] else [difference[num] + 1, index + 1]
            difference[target-num] = index
        return []


        