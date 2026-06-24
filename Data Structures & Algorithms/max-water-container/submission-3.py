class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1
        maxArea = 0
        while left<right:
            currentArea = min(heights[left], heights[right]) * (right-left)
            maxArea = max(maxArea, currentArea)
            if heights[right] > heights[left]:
                left+=1
            else:
                right-=1
        return maxArea    