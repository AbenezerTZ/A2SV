class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        ans = []
        res = []
        for i in range(rows):
            for j in range(cols):
                temp = []
                temp.append(abs(i - rCenter) + abs(j - cCenter))
                temp.append(i)
                temp.append(j)
                ans.append(temp)
        ans.sort()
        for i in range(len(ans)):
            res.append(ans[i][1:])
        return res
        
        