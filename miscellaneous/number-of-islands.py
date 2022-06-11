class Solution(object):
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        m, n, res = len(grid), len(grid[0]), 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    print(i, j)
                    self.dfs(grid, i, j)
                    res += 1
        
        return res
    
    def dfs(self, grid, i, j):
        grid[i][j] = '0'
        m, n = len(grid), len(grid[0])
        
        for d in self.directions:
            x, y = i + d[0], j + d[1]
            
            if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == '1':
                self.dfs(grid, x, y)


if __name__ == '__main__':
    s = Solution()
    grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
    print(s.numIslands(grid))