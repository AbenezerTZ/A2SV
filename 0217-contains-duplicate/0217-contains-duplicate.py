class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new = {}
        for i in nums:
            if i in new:
                new[i] += 1
            else:
                new[i] = 1
        if any(value > 1 for value in new.values()):
            return True
        else:
            return False
        