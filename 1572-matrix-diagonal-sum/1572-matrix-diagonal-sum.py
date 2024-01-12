class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        res = 0
        count = 0
        for i in range(len(mat)):
            res += mat[i][i]
            res += mat[i][len(mat)-1-count]
            count += 1
        if len(mat)%2 == 0:
            return res
        else:
            return res - mat[len(mat)//2][len(mat)//2]  