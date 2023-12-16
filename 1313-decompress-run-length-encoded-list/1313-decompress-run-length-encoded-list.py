class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        i = 0
        for j in nums[1:len(nums):2]:
            for _ in range(nums[i]):
                result.append(j)
            i+=2
        return result
        