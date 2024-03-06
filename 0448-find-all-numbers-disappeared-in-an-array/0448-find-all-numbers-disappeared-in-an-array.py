class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        exist = {}
        for i in range(1,len(nums)+1):
            exist[i] = 0
        for j in range(len(nums)):
            exist[nums[j]] += 1
        for key,value in exist.items():
            if value == 0:
                ans.append(key)
        return ans