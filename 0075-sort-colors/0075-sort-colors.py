class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = Counter(nums)
        j = 0
        for i in range(3):
            if i in freq:
                nums[j:freq[i]+j] = [i] * freq[i]
                j += freq[i]