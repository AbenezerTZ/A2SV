class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        row = []
        col = []
        for i in range(len(grid)):
            row.append(grid[i].count(1))
        for i in range(len(grid[0])):
            count = 0
            for j in range(len(grid)):
                if grid[j][i]==1:
                    count+=1
            col.append(count)
        for i in range(len(grid)): 
            temp = []
            for j in range(len(grid[0])): 
                n = row[i] + col[j] - (len(grid[0])-row[i]) - (len(grid)-col[j])
                temp.append(n)
            res.append(temp)
        return res
        


