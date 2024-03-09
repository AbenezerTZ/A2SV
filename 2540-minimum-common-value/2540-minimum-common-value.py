class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        freq = Counter(nums1)
        for i in nums2:
            if i in freq:
                return i
        return -1