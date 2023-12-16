class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            res = res + s[indices.index(i)]
        return res