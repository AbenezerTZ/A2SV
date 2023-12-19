class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        i = 1
        while i < n:
            i = i * 4
        if i==n or i/4==n:
            return True
        else:
            return False