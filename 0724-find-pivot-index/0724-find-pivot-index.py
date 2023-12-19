class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=sum(nums)
        left_sum=0
        for i in range (len(nums)):
            if left_sum==total-left_sum-nums[i]:
                return i
            else:
                left_sum+=nums[i]
                i+=1
        return -1