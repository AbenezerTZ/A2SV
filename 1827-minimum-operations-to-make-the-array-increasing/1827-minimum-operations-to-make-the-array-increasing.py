class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=i=0
        while i<len(nums)-1:
            if nums[i]<nums[i+1]:
                i+=1
            else:
                count=count+(nums[i]-nums[i+1]+1)
                nums[i+1]=nums[i]+1
                i+=1
        return count
        