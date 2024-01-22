class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        maxi = 0
        for i in range(len(n)):
            maxi = max(int(n[i]),maxi)
        return maxi