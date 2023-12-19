class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=list(str(x))
        i,j=0,len(x)-1
        while i<=j:
            if x[i]!=x[j]:
                return False
            i+=1
            j-=1
        return True