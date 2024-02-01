class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i+1] - nums[i] > k:
        #         return ans
        for i in range(0,len(nums),3):
            temp = nums[i:i+3]
            ans.append(temp)
        for i in range(len(ans)):
            if (ans[i][2] - ans[i][0]) > k:
                return []
        return ans
                  