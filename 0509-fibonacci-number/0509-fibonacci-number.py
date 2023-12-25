class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo ={}
        def dp(n):
            if n in memo:
                return memo[n]
            if n==0:
                return 0
            if n==1 or n==2:
                return 1
            else:
                result = dp(n-1) + dp(n-2)
            memo[n] = result
            return result 
        return dp(n)