class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        freq = Counter(nums)
        for i, j in freq.items():
            if j == 2:
                ans.append(i)
                break
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        for i in range(1, len(nums)+1):
            if nums[i-1] != i:
                ans.append(i)
                return ans
        ans.append(len(nums)+1)
        return ans

