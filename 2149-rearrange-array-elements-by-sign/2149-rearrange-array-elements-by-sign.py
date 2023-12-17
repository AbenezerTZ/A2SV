class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0]*len(nums)
        p = i = 0
        n = 1
        while i<len(nums) :  
            if nums[i]>0:
                res[p]=nums[i]
                p+=2
            else:
                res[n]=nums[i]
                n+=2
            i+=1
        return res
