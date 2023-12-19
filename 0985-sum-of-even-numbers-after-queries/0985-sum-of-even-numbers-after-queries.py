class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        s = 0
        
        for i in nums:
            if i % 2 == 0: s+=i
        res = []
        for x,y in queries:
            if nums[y]%2 == 0:
                s-= nums[y]
            nums[y]+=x
            if nums[y]%2 == 0:
                s+=nums[y]
            res.append(s)
        return res
            
