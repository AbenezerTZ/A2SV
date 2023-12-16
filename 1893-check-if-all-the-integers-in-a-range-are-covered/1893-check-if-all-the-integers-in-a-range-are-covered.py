class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        total = []
        n = 0
        while n<len(ranges):
            for i in range(ranges[n][0],ranges[n][1] + 1):
                total.append(i)
            n+=1
        for i in range(left,right+1):
            if i not in total:
                return False
        return True