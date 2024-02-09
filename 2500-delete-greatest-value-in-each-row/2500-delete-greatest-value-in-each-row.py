class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
        for i in range(len(grid[0])):  
            maxi = grid[0][i]
            for j in range(len(grid)):
                maxi = max(maxi,grid[j][i])
            count += maxi
        return count
        