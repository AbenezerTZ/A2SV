class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        ans = []
        while i < len(nums):
            if nums[i] == i+1 or nums[i]==nums[nums[i]-1]: 
                i += 1
            else:
                nums[nums[i]-1], nums[i] = nums[i],nums[nums[i]-1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(nums[i])
        return ans