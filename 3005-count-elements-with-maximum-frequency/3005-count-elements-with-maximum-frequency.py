class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxi = max(freq.values())
        count = 0
        for i in freq.values():
            if i == maxi:
                count += 1
        return count*maxi
        