class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        even_zero = 0
        odd_zero = 0
        even_one = 0
        odd_one = 0
        s = list(s)
        for i in range(len(s)):
            if s[i]=="0" and (i+1)%2==0:
                even_zero += 1
            elif s[i]=="0" and (i+1)%2==1:
                odd_zero += 1
            elif s[i]=="1" and (i+1)%2==0:
                even_one += 1
            elif s[i]=="1" and (i+1)%2==1:
                odd_one += 1    
        return (min(even_zero,odd_zero) + min(even_one,odd_one))
        