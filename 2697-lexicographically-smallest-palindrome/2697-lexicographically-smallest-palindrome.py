class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] < s[j]:
                s[j] = s[i]
            elif s[i] > s[j]:
                s[i] = s[j]                
            i += 1
            j -= 1
        return "".join(s)