class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        s = str(num)
        count = 0
        for i in range(len(s) - k + 1):
            if int(s[i:i+k]) != 0 and num % int(s[i:i+k]) == 0:
                count += 1
        return count
        