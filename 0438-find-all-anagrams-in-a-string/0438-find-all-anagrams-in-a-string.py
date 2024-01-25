class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        p = list(p)
        p.sort()
        for i in range(len(s)-len(p)+1):
            n = list(s[i:i+len(p)])
            n.sort()
            if n == p:
                ans.append(i)
        return ans
         
        