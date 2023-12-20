class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxi = float('-inf') 
        for i in range(0,len(grid)-2):  
            for j in range(1,len(grid[0])-1): 
                temp = grid[i][j-1] + grid[i][j] + grid[i][j+1] + grid[i+1][j] + grid[i+2][j-1] + grid[i+2][j] + grid[i+2][j+1]
                maxi = max(maxi,temp)
        return maxi