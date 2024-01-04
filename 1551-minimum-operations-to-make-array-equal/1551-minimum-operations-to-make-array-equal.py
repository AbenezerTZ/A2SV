class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = n - 1
        count = 0
        while i > 0 :
            count += i
            i -= 2
        return count
            
