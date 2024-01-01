class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        rev = []
        non = []
        ans = []
        for i in range(0,len(s),(2*k)): 
            rev.append(s[i:i+k][::-1])
        for j in range(k,len(s),(2*k)):
            non.append(s[j:j+k])
        n = min(len(non),len(rev))
        for i in range(n):
            ans.append(rev[i])
            ans.append(non[i])
        if len(non)==len(rev):
            return ("".join(ans))
        else:
            ans.append(rev[-1])
            ans = "".join(ans)
            return ("".join(ans))
            
            
            
            
        