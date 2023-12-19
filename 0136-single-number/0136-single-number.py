class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new={}
        for i in nums:
            if i in new:
                new[i]+=1
            else:
                new[i]=1
        return [key for key,value in new.items() if value==1][0]        