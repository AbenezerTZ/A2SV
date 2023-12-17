class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1=set(nums1)
        nums2=set(nums2)
        answer=[]
        f1=nums1.difference(nums2)
        f1=list(f1)
        answer.append(f1)
        f2=nums2.difference(nums1)
        f2=list(f2)
        answer.append(f2)
        return answer
        