class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            elif i not in count:
                count[i]=1
        return max(count, key=count.get)  