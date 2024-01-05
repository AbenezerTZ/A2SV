class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        for num in nums:
            if not ans or num > ans[-1]:
                ans.append(num)
            else:
                count = 0
                while count < len(ans) and num > ans[count]:
                    count += 1
                ans[count] = num
        return len(ans)