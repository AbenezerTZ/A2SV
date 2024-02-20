class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check = [i for i in range(0,len(nums)+1)]
        check = set(check)
        nums = set(nums)
        temp = list(check.symmetric_difference(nums))
        
        return temp[0]