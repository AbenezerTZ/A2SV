class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=0
        if len(nums)==1:
            return True
        elif len(nums)>=2 and nums[0]>nums[1]:
            nums[0]=nums[1]
            count+=1
        for i in range(len(nums)-1): # 0 1
            if nums[i]>nums[i+1] and nums[i+1]>=nums[i-1] :
                nums[i]=nums[i+1]
                count+=1
            elif nums[i]>nums[i+1] and nums[i+1]<nums[i-1]:
                nums[i+1]=nums[i]
                count+=1
        print(count)
        if count<=1:
            return True
        else:
            return False