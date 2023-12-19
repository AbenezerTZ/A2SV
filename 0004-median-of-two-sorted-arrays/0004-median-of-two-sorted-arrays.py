class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float 
        """
        final = nums1 + nums2
        final.sort()
        if len(final)%2==0:
            return (float(final[len(final)/2] + final[(len(final)/2)-1]) / 2 ) 
        else:
            return (final[(len(final)-1)/2])
        