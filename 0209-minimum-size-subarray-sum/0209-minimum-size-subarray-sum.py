class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if target in nums:
            return 1
        elif sum(nums) < target:
            return 0
        
        window = nums[0]
        count = 1
        mini = float('inf')
        j = 0
        i = 1
        while i <= len(nums) : 
            if window < target and i < len(nums): 
                count += 1
                window += nums[i]
                i += 1
            elif window >= target:            
                mini = min(mini,count)
                count -= 1
                window -= nums[j]
                j += 1
            else:
                break
        return mini
                
        