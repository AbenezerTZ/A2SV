class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        i = j = 0
        k = 0
        while len(ans)!= len(matrix)*len(matrix[0]):
            while j < len(matrix[0]) - k:
                ans.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1
            while len(ans)!= len(matrix)*len(matrix[0]) and i < len(matrix) - k:
                ans.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            while len(ans)!= len(matrix)*len(matrix[0]) and j >= k:
                ans.append(matrix[i][j])
                j -= 1
            j += 1
            i -= 1
            while len(ans)!= len(matrix)*len(matrix[0]) and i >= k+1:
                ans.append(matrix[i][j])
                i -= 1
            i += 1
            j += 1
            k += 1
        return ans