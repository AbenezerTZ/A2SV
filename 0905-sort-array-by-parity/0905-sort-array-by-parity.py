class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in nums:
            if i%2==0:
                result.insert(0,i)
            else:
                result.append(i)
        return result
        