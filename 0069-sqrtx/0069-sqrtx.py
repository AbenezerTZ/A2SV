class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i=result=0
        while result < x:
            i+=1
            result=i*i
        if result > x:
            return i-1
        else:
            return i
