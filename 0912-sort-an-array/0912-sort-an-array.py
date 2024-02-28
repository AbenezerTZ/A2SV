class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        maxi = nums[0]
        mini = nums[0]
        ans = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                if i > maxi:
                    maxi = i
                if i < mini:
                    mini = i
        for n in range(mini,maxi+1):
            if n in freq:
                for _ in range(freq[n]):
                    ans.append(n)
        return ans
                
                
        