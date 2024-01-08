class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = 0
        temp = nums[-1]
        for i in range(k):
            count += temp
            temp += 1
        return count
        