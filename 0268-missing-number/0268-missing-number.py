class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        while i<len(nums) and i==nums[i]:
            i+=1
        return i
        