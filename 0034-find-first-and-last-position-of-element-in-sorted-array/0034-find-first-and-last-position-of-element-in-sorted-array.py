class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x=len(nums)
        for i in range(x):
            if nums[i]==target:
                nums.append(i)
        if len(nums)==x:
            return ([-1,-1])
        else:
            nums.append(min(nums[x::]))
            nums.append(max(nums[x::]))
            return nums[-2::]