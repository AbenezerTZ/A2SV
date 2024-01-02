class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        freq = Counter(nums)
        ans = [[] for _ in range(max(freq.values()))]
        for key,value in freq.items():
            for i in range(value):
                ans[i].append(key)     
        return ans
                