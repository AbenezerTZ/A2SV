class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        tracker = {}
        for a,b in enumerate(nums):
            tracker[b] = a
        for b,y in operations:
            i = tracker[b]
            nums[i] = y
            tracker[y] = i
            del tracker[b]
        return nums