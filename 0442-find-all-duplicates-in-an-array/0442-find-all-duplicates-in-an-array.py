class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==1:
            return []
        nums.sort()
        ans = []
        i = 0
        j = 1
        while j < len(nums):
            if nums[i]==nums[j]:
                ans.append(nums[i])
            i += 1
            j += 1
        return ans