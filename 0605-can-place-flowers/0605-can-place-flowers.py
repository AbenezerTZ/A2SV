class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        max=0
        i=0
        while i<len(flowerbed):
            if flowerbed[i]==0:
                if i==0 or flowerbed[i-1]==0:
                    if i==len(flowerbed)-1 or flowerbed[i+1]==0:
                        flowerbed[i]=1
                        max+=1
            i+=1
        if max>=n:
            return True
        return False 

        