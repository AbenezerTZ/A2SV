class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        nums = [i for i in range(1,n+1)]
        left = sum(nums[:(n//2)])
        right = sum(nums[(n//2)-1:])
        temp = (n//2)
        while right > left:
            left += nums[temp]
            right -= nums[temp-1]
            if right == left:
                return nums[temp]
            temp += 1
        return -1