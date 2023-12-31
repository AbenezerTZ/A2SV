class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxi = -1
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    maxi = max(maxi,abs(i-j)-1)
        return maxi
                
            
        