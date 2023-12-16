class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sort = sorted(nums)
        temp ={}
        smallerNum = []
        for i in range(len(sort)):
            if sort[i] not in temp:
                temp[sort[i]]=i
        for i in nums:
            smallerNum.append(temp[i])
        return smallerNum