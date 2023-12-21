class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        i = 0
        j = 1
        if len(mat[0])==1:
            for i in range(len(mat)): 
                ans.append(mat[i][0])
            return ans
        elif len(mat)==1:
            return mat[0]
        
        ans.append(mat[0][0])
        while len(ans) != (len(mat) * len(mat[0]))-1:
            while i <= len(mat)-1 and j >= 0: 
                ans.append(mat[i][j])
                i += 1
                j -= 1
            if j < 0 and i <= len(mat)-1:
                j += 1
            elif i > len(mat)-1 and j>=0:
                i -= 1
                j += 2
            elif j < 0 and i > len(mat)-1:
                j += 2
                i -= 1
            if len(ans) == (len(mat) * len(mat[0]))-1:
                ans.append(mat[len(mat)-1][len(mat[0])-1])
                return ans
                
            while i >= 0 and j <= len(mat[0])-1:
                ans.append(mat[i][j])
                i -= 1
                j += 1
            if i < 0 and j <= len(mat[0])-1:
                i += 1
            elif i >= 0 and j > len(mat[0])-1:
                j -= 1
                i += 2
            elif i < 0 and j > len(mat[0])-1:  # the new change
                j -= 1
                i += 2      
        ans.append(mat[len(mat)-1][len(mat[0])-1])
        return ans