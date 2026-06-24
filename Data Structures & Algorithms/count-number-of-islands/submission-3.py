class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        visited = set()
        islandcount = 0
        def dfs(coord: Tuple[int, int]):
            visited.add(coord)
            for direction in [(0,1), (1,0), (-1, 0), (0,-1)]:
                newcoord = (coord[0] + direction[0], coord[1] + direction[1])
                if newcoord[0] >= 0 and newcoord[1]>= 0 and newcoord[0] <height and newcoord[1]<width and newcoord not in visited and grid[newcoord[0]][newcoord[1]]=="1":
                    dfs(newcoord)
        for rowindex, row in enumerate(grid):
            for column, value in enumerate(row):
                if grid[rowindex][column] == "1" and (rowindex, column) not in visited:
                    islandcount +=1
                    dfs((rowindex,column))
        return islandcount




        