class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        newheights = sorted(heights)
        count = 0
        for index, height in enumerate(heights):
            if height != newheights[index]:
                count+=1
        return count
        