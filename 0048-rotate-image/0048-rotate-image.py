class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        count = 0
        i = j = 0
        for _ in range(len(matrix)//2):            
            for _ in range(len(matrix)-1-count):
                temp1 = matrix[i][j]
                
                for r in range(0+i,len(matrix[0])-1-j):
                    temp2 = matrix[0+i][r+1]
                    matrix[0+i][r+1] = temp1
                    temp1 = temp2
                

                for d in range(1+i,len(matrix[0])-j):
                    temp2 = matrix[d][len(matrix)-1-j]
                    matrix[d][len(matrix)-1-j] = temp1
                    temp1 = temp2
        

                for l in range(len(matrix[0])-2-i,-1+j,-1):
                    temp2 = matrix[len(matrix)-1-i][l]
                    matrix[len(matrix)-1-i][l] = temp1
                    temp1 = temp2
            

                for u in range(len(matrix[0])-2-i,-1+j,-1):
                    temp2 = matrix[u][0+j]
                    matrix[u][0+j] = temp1
                    temp1 = temp2
            
            i += 1
            j += 1
            count += 2

                
                
                
                