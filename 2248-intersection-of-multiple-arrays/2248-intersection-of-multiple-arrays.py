class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        temp = len(nums)
        freq = {}
        for i in range(temp):
            for j in range(len(nums[i])):
                if nums[i][j] in freq:
                    freq[nums[i][j]] += 1
                else:
                    freq[nums[i][j]] = 1
        ans = []
        for key , value in freq.items():
            if value == temp:
                ans.append(key)
        ans.sort()
        return ans
            
        