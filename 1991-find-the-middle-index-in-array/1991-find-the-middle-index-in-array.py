class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: 
            return 0
        for i in range(len(nums)):
            if i == 0:
                if sum(nums[i+1:]) == 0:
                    return i
            elif i == len(nums)-1:
                if sum(nums[:i]) == 0:
                    return i
            else:
                if sum(nums[:i]) == sum(nums[i+1:]):
                    return i
        return -1
     