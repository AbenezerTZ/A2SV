class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        max_count=0
        for right,i in enumerate(nums):
            if i==0:
                left=right+1
            max_count=max(max_count,right-left+1)
        return max_count