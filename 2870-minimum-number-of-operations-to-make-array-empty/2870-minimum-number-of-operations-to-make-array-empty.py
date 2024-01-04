class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        freq = Counter(nums)
        if 1 in freq.values():
            return -1
        for key,value in freq.items():
            if value == 2:
                count += 1
            elif value%3 == 0:
                count += value/3
            elif value%3 == 1:
                count += (value//3 - 1) + 2
            elif value%3 == 2:
                count += (value//3 - 1) + 2
        return count
                