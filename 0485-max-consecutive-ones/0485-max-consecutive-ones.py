class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums.count(0)==1:
            maxi = len(nums)-(nums.index(0)+1)
            return max(maxi,len(nums)-maxi-1)
        check = ''.join(map(str,nums))
        count=len(check)
        while count>0:
            if "1"*count in check:
                return count
            else:
                count-=1
        return 0
