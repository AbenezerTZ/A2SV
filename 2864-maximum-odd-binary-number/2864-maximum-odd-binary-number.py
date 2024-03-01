class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        zero = 0
        one = 0

        for char in s:
            if char == '0': 
                zero += 1
            else: 
                one += 1
        ans = '1' * (one - 1) + '0' * zero + '1'
        return ans