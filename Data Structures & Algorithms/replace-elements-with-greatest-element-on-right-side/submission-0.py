class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = arr[len(arr) - 1]
        arr[len(arr)-1] = -1
        for i in range(len(arr)-2,-1, -1):
            temp = arr[i]
            arr[i] = maxNum
            maxNum = max(maxNum, temp)
        return arr 
