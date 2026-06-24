class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        directions = [(0,1), (1,0), (-1,0), (0, -1)]
        height = len(grid)
        width = len(grid[0])
        queue = deque()
        for cr in range(height):
            for cw in range(width):
                if grid[cr][cw] == 0:
                    queue.append((cr,cw, 0))
        while queue:
            cr, cw, distance = queue.popleft()
            for direction in directions:
                nr, nw = cr + direction[0], cw + direction[1]
                if 0<=nr<height and 0<=nw<width and grid[nr][nw] != -1:
                    if grid[nr][nw] > distance + 1:
                        grid[nr][nw] = distance + 1
                        queue.append((nr,nw, distance + 1))

