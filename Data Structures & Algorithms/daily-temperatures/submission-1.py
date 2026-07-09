from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        numdays = len(temperatures)
        stack = deque()
        res = [0]*numdays
        for day, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > temperatures[stack[-1]]:
                resolveday = stack.pop()
                res[resolveday] = day - resolveday
            stack.append(day)
            
        return res

        