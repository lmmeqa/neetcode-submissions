class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in board:
            for val in row:
                if val != "." and val in seen:
                    return False
                seen.add(val)
            seen.clear()
        for column in range(9):
            for row in range(9):
                val = board[row][column]
                if val != "." and val in seen:
                    return False
                seen.add(val)
            seen.clear()
        for row in range(0,9,3):
            for column in range(0,9,3):
                for rowinsquare in range(3):
                    for valinsquare in range(3):
                        val = board[row + rowinsquare][column + valinsquare]
                        if val != "." and val in seen:
                            return False
                        seen.add(val)
                seen.clear()
        return True
        
        
