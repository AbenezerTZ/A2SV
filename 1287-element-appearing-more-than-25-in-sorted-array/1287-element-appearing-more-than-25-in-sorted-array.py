class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        i = 0
        while i<len(arr):
            if arr.count(arr[i])<=len(arr)/4:
                i+=arr.count(arr[i])
            else:
                return arr[i]
        