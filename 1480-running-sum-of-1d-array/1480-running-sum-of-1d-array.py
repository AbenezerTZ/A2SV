class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = 0
        for i in range(len(nums)):
            nums[i] += n
            n = nums[i]
        return nums