class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = [[-1] * 2 for _ in range(len(s))]
        memo.append([1, 1])

        def dp(index, val):
            if len(val) == 2 or val == '0':
                if int(val) > 26 or val == '0':
                    return 0
                val = ''

            if memo[index] [len(val)] == -1:
                memo[index] [len(val)] = dp(index + 1, val + s[index]) + (dp(index + 1, s[index]) if val else 0)
            return memo[index] [len(val)]
        
        return dp(0, '')