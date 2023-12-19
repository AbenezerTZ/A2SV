class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t = list(t) 
        s = list(s)
        t.sort()
        s.sort() 
        for i in s:
            t.remove(i)
        return t[0]
        