from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(0,1), (1,0), (-1, 0), (0,-1)]
        height = len(grid)
        width = len(grid[0])
        queue = deque()
        freshcount = 0

        minutes = 0

        for row in range(0, height):
            for column in range(0, width):
                if grid[row][column] == 2:
                    queue.append((row, column, 0))
                if grid[row][column] == 1:
                    freshcount+=1
        while queue:
            row, column, distance = queue.popleft()
            for dr, dc in DIRECTIONS:
                nr, nc = row +dr, column + dc
                if 0<=nr<height and 0<=nc<width and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    freshcount -=1
                    minutes = max(minutes, distance + 1)
                    queue.append((nr, nc, distance + 1))

        return minutes if freshcount == 0 else -1
        