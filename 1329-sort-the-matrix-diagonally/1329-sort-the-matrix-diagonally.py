class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        diag = []
        for i in range(len(mat) - 1,-1,-1):
            order = []
            temp = a = i
            j = b = 0
            order.append(mat[temp][j])
            temp += 1
            j += 1
            while temp < len(mat) and j < len(mat[0]):
                order.append(mat[temp][j])
                temp += 1
                j += 1
            i -= 1
            order.sort()
            for n in range(len(order)):
                mat[a][b] = order[n]
                a += 1
                b += 1
        j = 1
        while j < len(mat[0]):
            order = []
            temp = b = j 
            i = a = 0
            order.append(mat[i][temp])
            temp += 1
            i += 1
            while temp < len(mat[0]) and i < len(mat):
                order.append(mat[i][temp])
                temp += 1
                i += 1
            order.sort()
            for n in range(len(order)):
                mat[a][b] = order[n]
                a += 1
                b += 1
            j += 1
        return mat  