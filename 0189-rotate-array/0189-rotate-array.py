class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last = nums[len(nums)-(k%len(nums)):]
        front = nums[:len(nums)-(k%len(nums))]
        for i in range(k%len(nums)):
            nums[i] = last[i]
        n = 0
        for j in range((k%len(nums)) ,len(nums)): 
            nums[j] = front[n]
            n += 1
        
        