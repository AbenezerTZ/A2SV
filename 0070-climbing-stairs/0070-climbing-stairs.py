class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def dp(s):
            if s==1:
                return 1
            elif s==2:
                return 2
            elif s in memo:
                return memo[s]
            else:
                result = dp(s-1) + dp(s-2)
                memo[s] = result
                return memo[s]
        return dp(n)