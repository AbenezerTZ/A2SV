class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        mini = float('inf')
        for i in range (len(points)):
            if points[i][0]==x and points[i][1]==y:
                return i
            elif points[i][0]==x or points[i][1]==y:
                mini = min(mini, abs(x-points[i][0]) + abs(y-points[i][1]))
        if mini == float('inf'):
            return -1
        for i in range (len(points)):
            if abs(x-points[i][0]) + abs(y-points[i][1]) == mini and (points[i][0]==x or points[i][1]==y) :
                return i
        
                