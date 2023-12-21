class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        maxi = float('-inf')
        points.sort()
        for i in range(len(points)-1): # 0 1 2 3 4  
            res = points[i+1][0] - points[i][0]
            maxi = max(res,maxi)
        return maxi
        