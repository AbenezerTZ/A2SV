class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        if len(grid) < 3 or len(grid[0]) < 3:
            return count
        
        for i in range(len(grid)-2): 
            for j in range(len(grid[0])-2):
                if sum(grid[i][j:j+3])==sum(grid[i+1][j:j+3])==sum(grid[i+2][j:j+3])==(grid[i][j]+grid[i+1][j]+grid[i+2][j])==(grid[i][j+1]+grid[i+1][j+1]+grid[i+2][j+1])==(grid[i][j+2]+grid[i+1][j+2]+grid[i+2][j+2])==(grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2])==(grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]): 
                    
                    freq = []
                    sub = [row[j:j+3] for row in grid[i:i+3]]
                    for m in range(3):
                        for n in range(3):
                            freq.append(sub[m][n])
                    freq.sort()
                    if freq == [1,2,3,4,5,6,7,8,9]:
                        count += 1
        return count
    