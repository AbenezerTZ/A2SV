class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        i = 0
        while i < len(arr)-1:
            if arr[i] < arr[i+1]:
                i += 1
            elif arr[i] == arr[i+1]:
                return False
            else:
                break
        if i+2==len(arr):
            return True
        if i+1==len(arr) or i == 0:
            return False
    
        while i < len(arr)-1:
            if arr[i] > arr[i+1]:
                i += 1
            elif arr[i] == arr[i+1] or arr[i] < arr[i+1]:
                return False
        return True
            