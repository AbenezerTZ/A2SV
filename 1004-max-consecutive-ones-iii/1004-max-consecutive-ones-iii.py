class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi = 0
        i = 0
        j = 0
        n = k
        count = 0
        while j < len(nums):   
            if nums[j] == 1:
                count += 1
                maxi = max(maxi,count)
                j += 1
            elif nums[j] == 0 and n != 0:
                count += 1
                maxi = max(maxi,count)
                j += 1
                n -= 1   
            elif nums[j] == 0 and n == 0:
                while i < j and nums[i] != 0:
                    i += 1
                    count -= 1     
                i += 1
                j += 1
        return maxi
                