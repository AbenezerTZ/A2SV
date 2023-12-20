class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0: return 0
        elif len(nums)==1: return 1
        nums.sort()
        i = 0
        maxi = float('-inf')
        count = 1
        while i < len(nums)-1:
            while i < len(nums)-1 and nums[i]+1==nums[i+1]:
                count+=1
                i+=1
            if i < len(nums)-1 and nums[i]==nums[i+1]:
                maxi = max(maxi,count)
                i+=1
            else:
                maxi = max(maxi,count)
                i+=1
                count = 1    
        return maxi
    # -1 -1 0 1 3 4 5 6 7 8 9 