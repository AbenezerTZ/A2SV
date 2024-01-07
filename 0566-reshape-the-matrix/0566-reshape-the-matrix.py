class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat)*len(mat[0])!= r*c:
            return mat
        row = []
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                row.append(mat[i][j])
        n = 0
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(row[n])
                n+=1
            ans.append(temp)
        return ans
        