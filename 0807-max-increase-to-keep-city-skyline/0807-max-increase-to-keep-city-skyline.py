class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_max = []
        col_max = []
        for i in range(len(grid)):
            row_max.append(max(grid[i]))
            c_max = 0
            for j in range (len(grid)):
                c_max = max(c_max,grid[j][i])
            col_max.append(c_max)
        count = 0 
        for i in range(len(grid)): 
            for j in range(len(grid)):
                if col_max[j] <= row_max[i]: 
                    count += col_max[j]-grid[i][j]
                else:
                    count += row_max[i]-grid[i][j]
        return count
                
        