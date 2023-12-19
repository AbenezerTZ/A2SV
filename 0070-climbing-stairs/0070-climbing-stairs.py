class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        num1=1
        num2=2
        current=0
        if n<3:
            return n
        for i in range(2,n):
            current=num1+num2
            num1=num2
            num2=current
        return current 