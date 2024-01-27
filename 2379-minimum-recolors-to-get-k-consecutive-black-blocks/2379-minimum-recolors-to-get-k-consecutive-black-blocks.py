class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        window = 0
        
        for i in range(k): 
            if blocks[i] == "B":
                window += 1
        maxi = window
        for j in range(1,len(blocks)-k+1):
            if blocks[j-1]=="B":
                window -= 1
            if blocks[j+k-1]=="B":
                window += 1
            maxi = max(maxi,window)
        return k - maxi
        