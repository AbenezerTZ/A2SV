class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1]
        maxi = 0
        for i in range(2,len(nums)):
            if res > nums[i]:
                maxi = max(maxi,res + nums[i])
                
            res += nums[i]
        if maxi != 0:
            return maxi 
        else:
            return -1