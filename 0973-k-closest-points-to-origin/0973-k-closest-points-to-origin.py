class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        closest = []
        for i in range(len(points)):
            temp = []
            ans = sqrt((points[i][0]**2) + (points[i][1]**2))
            temp.append(ans)
            temp.append(i)
            res.append(temp)
        res.sort()
        for i in range(k):
            closest.append(points[res[i][1]])
        return closest