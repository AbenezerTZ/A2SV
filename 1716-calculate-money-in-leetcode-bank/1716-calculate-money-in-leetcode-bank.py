class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        total = 0
        while n!=0:
            if n-7>=0:
                total = total + sum(range(count,count+7))
                n-=7
                count+=1
            else:
                total += sum(range(count,count+n))
                n=0
        return total

        
