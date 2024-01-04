class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(i for i in range(n - 1, 0 , -2))
            
