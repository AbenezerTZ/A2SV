class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        memo = {}
        def total (n, target):
            if n == 0:
                if target == 0:
                    return 1
                else:
                    return 0
            if (n,target) in memo:
                return memo [(n, target)]
            res = 0
            for i in range(1,k + 1):
                res = (res + total(n-1,target - i)) % MOD
            memo[(n,target)] = res
            return res
        return total(n,target)
        