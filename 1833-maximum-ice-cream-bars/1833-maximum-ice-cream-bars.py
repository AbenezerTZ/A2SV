class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        count=0
        costs.sort()
        for i in costs:
            coins-=i
            if coins>0:
                count+=1
            elif coins==0:
                count+=1
                break
            else:
                break
        return count
            


        