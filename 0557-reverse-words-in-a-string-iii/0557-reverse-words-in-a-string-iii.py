class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split(" ")
        result=[i[::-1] for i in s]
        rev=" ".join(result)
        return rev