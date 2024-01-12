class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        count = 0
        left = {0:0}
        right = {len(nums):0}
        
        for i in range(1,len(nums)):
            if nums[i-1]==0:
                count += 1
            left[i] = count
        if nums[-1]==0:
            left[len(nums)]=count+1
        else:
            left[len(nums)]=count
            
        count = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==1:
                count += 1
            right[i] = count
            
        maxi = 0
        for key,value in left.items():
            maxi = max(maxi, left[key]+right[key])
        for key,value in left.items():
            if left[key]+right[key] == maxi:
                ans.append(key)
        return ans

        
        