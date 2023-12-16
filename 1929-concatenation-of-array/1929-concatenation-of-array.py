class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        conc = nums[:]
        for i in nums:
            conc.append(i)
        return conc
        