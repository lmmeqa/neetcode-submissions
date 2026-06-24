class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchRow(rownum: int):
            row = matrix[rownum]
            low = 0
            high = len(row) - 1

            while low <= high:
                mid = (high + low)//2
                if row[mid] == target:
                    return True
                if row[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False
        low = 0
        high = len(matrix) - 1
        
        if target > matrix[high][0]:
            return searchRow(high)
        while low < high:
            mid = (low + high + 1)//2
            if matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid 
        
        return searchRow(low)



        
                