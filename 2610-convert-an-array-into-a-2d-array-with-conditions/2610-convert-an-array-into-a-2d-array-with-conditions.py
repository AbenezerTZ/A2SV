class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        ans = [[] for _ in range(max(freq.values()))]
        for key,value in freq.items():
            for i in range(value):
                ans[i].append(key)     
        return ans
                