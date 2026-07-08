from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        seen = set()
        def dfs(coord):
            seen.add(coord)
            if len(seen) == len(word):
                return True
            DIRECTIONS = [(0,1),(1,0), (-1,0), (0,-1)]
            for direction in DIRECTIONS:
                nr,nc = coord[0] + direction[0], coord[1] + direction[1]
                if 0<=nr<len(board) and 0<=nc<len(board[0]) and (nr,nc) not in seen and word[len(seen)] == board[nr][nc]:
                    
                    if dfs((nr,nc)):
                        return True
            seen.remove(coord)
            return False
                    
        for rownum, row in enumerate(board):
            for colnum, value in enumerate(row):
                if board[rownum][colnum] == word[0] and dfs((rownum,colnum)):
                    return True
        return False



                
