class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1 or sum(nums) - nums[0] == 0:
            return 0
        left = []
        right = []
        left_temp = 0
        right_temp = 0
        for i in range(len(nums)):
            left_temp += nums[i]
            right_temp += nums[len(nums)-1-i]
            left.append(left_temp)
            right.append(right_temp)
        for i in range(len(left)):
            if left[i] == right[len(right)-1-i]:
                return i
        return -1
