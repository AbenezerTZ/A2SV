class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        maxi = max(freq.values())
        count = 0
        for i in freq.values():
            if i == maxi:
                count += 1
        return count*maxi
        