class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        total = 0
        for i in nums:
            if i%2==0: total+=i
        ans = []

        for x, k in queries:
            if nums[k] % 2 == 0: total -= nums[k]
            nums[k] += x
            if nums[k] % 2 == 0: total += nums[k]
            ans.append(total)

        return ans
       
