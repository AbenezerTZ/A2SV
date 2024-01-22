class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        maxi = float('-inf')
        i = 0
        j = len(nums) - 1
        while i < j:
            maxi = max(maxi , nums[i]+nums[j])
            i += 1
            j -= 1
        return maxi