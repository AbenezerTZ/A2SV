class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x1 = min(nums)
        nums.remove(x1)
        x2 = min(nums)
        y1 = max(nums)
        nums.remove(y1)
        y2 = max(nums)
        return (y1*y2)-(x1*x2)