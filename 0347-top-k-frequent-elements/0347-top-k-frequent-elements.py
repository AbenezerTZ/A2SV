class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        pair = []
        freq = Counter(nums)
        for a,b in freq.items():
            temp = []
            temp.append(b)
            temp.append(a)
            pair.append(temp)
        pair.sort(reverse=True)
        for i in range(k):
            ans.append(pair[i][1])
        return ans        