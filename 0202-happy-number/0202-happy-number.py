class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        total=0
        count=0
        if n==1:
            return True
        else:
            while n!=1 and count<=2^31-1:
                count+=1
                n=list(str(n))
                for i in n:
                    n=int(i)*int(i)
                    total+=n
                if total==1:
                    n=1
                    return True
                else:
                    n=total
                    total=0
            return False

        