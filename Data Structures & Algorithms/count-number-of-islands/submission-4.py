from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
        width = len(grid)
        height = len(grid[0])
        count = 0


        def floodfill(coord):
            queue = deque()
            queue.append(coord)
            while queue:
                coord = queue.popleft()
                seen.add(coord)
                for direction in DIRECTIONS:
                    nr,nc = coord[0] + direction[0], coord[1] + direction[1]
                    if 0<=nr<width and 0<=nc<height and grid[nr][nc] == "1" and (nr,nc) not in seen:
                        queue.append((nr,nc))


        for rownum, row in enumerate(grid):
            for colnum, value in enumerate(row):
                coord = (rownum,colnum)
                if value == "1" and coord not in seen:
                    count+=1
                    floodfill(coord)
        return count
                    

        