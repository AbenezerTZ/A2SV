class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in row:
                        row.append(i)
                    if j not in col:
                        col.append(j)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in col:
            for j in range(len(matrix)):
                matrix[j][i] = 0
            
            
                