class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        freq = Counter(arr)
        nums = []
        for a,b in freq.items():
            nums.append(b)
        nums.sort()
        res = k
        count = 0
        for i in range(len(nums)):
            res -= nums[i]
            count += 1
            if res < 0:
                return len(nums) - count + 1
            elif res == 0:
                return len(nums) - count                