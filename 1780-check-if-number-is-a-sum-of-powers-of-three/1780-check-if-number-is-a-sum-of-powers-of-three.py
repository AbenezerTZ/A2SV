class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m=3
        nums=[]
        while m<=n:
            powers=1
            while m*3<=n:
                m=m*3
                powers+=1
            if powers not in nums:
                nums.append(powers)
            else:
                return False
            n=n-m
            m=3
        if n==1 or n==3 or n==0:
            return True
        else:
            return False