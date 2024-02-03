class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        count = 0
        total = 0
        freq = Counter(banned)
        nums = [i for i in range (1,n+1)]
        for i in range(len(nums)):
            if nums[i] not in freq:
                total += nums[i]
                if total <= maxSum:
                    count += 1
                else:
                    return count
        return count