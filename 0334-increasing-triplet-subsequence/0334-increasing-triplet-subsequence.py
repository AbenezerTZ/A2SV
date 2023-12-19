class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x=float('inf')
        y=float('inf')
        for num in nums:
            if num<=x:
                x=num
            elif num<=y:
                y=num
            else:
                return True
        return False