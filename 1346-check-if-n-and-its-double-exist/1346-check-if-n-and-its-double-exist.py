class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        for i in arr:
            if i == 0:
                count+=1
        if count>=2:
            return True
        for i in arr:
            if (i*2) in arr and arr.index(i)!=arr.index(i*2):
                return True
        return False
        