class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        totalwater = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        while left<right:
            if leftMax < rightMax:
                totalwater += leftMax - height[left]
                left+=1
                leftMax = max(leftMax, height[left])
            else:
                totalwater += rightMax - height[right]
                right-=1
                rightMax = max(rightMax, height[right])
        return totalwater
            
            
