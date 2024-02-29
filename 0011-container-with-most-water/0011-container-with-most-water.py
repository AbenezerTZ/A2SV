class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        n = len(height)-1
        maxi = 0
        while i < j:
            if height[i] < height[j]:
                maxi = max(maxi,height[i]*n)
                i += 1
            else:
                maxi = max(maxi,height[j]*n)
                j -= 1
            n -= 1
        return maxi
                