class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words=s.split(" ")
        if len(words)!=len(pattern):
            return False
        p_s={}
        s_p={}
        for i,j in zip(pattern,words):
            if i in p_s and p_s[i]!=j:
                return False
            if j in s_p and s_p[j]!=i:
                return False
            p_s[i]=j
            s_p[j]=i
        return True