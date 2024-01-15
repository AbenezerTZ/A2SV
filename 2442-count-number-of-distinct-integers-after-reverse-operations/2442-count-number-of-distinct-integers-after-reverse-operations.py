class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        for i in range(len(nums)):
            if len(str(nums[i])) == 1:
                ans.append(nums[i])
            else:
                temp = str(nums[i])[::-1]
                ans.append(int(temp))
        nums.extend(ans)
        return len(set(nums))