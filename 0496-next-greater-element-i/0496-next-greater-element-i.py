class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in range(len(nums1)):
            n=nums2.index(nums1[i])
            if n==len(nums2)-1:
                result.append(-1)
            else:
                x=len(result)
                for j in range(n,len(nums2)):
                    if nums1[i]<nums2[j]:
                        result.append(nums2[j])
                        break
                if x==len(result):
                    result.append(-1)
        return result

                