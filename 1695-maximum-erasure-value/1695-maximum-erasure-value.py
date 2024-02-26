class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        i = j = 0
        maxi = 0
        temp = 0
        while j < len(nums):
            if nums[j] not in freq or freq[nums[j]] == 0:
                freq[nums[j]] = 1
                temp += nums[j]
                maxi = max(maxi, temp)
                j += 1
            else:
                while nums[i] != nums[j]: 
                    temp -= nums[i]
                    freq[nums[i]] -= 1
                    i += 1
                i += 1
                j += 1
        return maxi
                
                
        