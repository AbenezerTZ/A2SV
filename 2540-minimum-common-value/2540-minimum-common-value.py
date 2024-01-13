class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        mini = -1
        nums1 = set(nums1)
        nums2 = set(nums2)
        common = nums1.intersection(nums2)
        common = list(common)
        if len(common) == 0:
            return -1
        else:
            return min(common)