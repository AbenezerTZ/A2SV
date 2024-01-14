class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        
        ans = ""
        combo = [str(i) for i in nums]
        combo.sort(key=lambda x: x * 10, reverse=True)
        ans = ''.join(combo)
        return str(int(ans))