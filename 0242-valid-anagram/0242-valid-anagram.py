class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=list(s)
        t=list(t)
        if len(s)!=len(t):
            return False
        else:
            for i in s:
                if i in t:
                    t.remove(i)
            if len(t)==0:
                return True
            else:
                return False
            