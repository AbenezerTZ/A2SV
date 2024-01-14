class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        uniqe = []
        count = 0
        for key in freq.keys():
            uniqe.append(key)
        uniqe.sort(reverse=True)
        for i in range(len(uniqe)-1):
            count += freq[uniqe[i]]
            freq[uniqe[i+1]] += freq[uniqe[i]]                       
        return count