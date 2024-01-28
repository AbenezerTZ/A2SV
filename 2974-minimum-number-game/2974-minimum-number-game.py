class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        alice = []
        bob = []
        ans = []
        nums.sort()
        for i in range(0,len(nums),2):
            alice.append(nums[i])
            bob.append(nums[i+1])
        for i in range(len(bob)):
            ans.append(bob[i])
            ans.append(alice[i])
        return ans
            