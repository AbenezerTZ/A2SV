class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i=0
        fixer=len(arr)
        count = 0
        while i < fixer :
            if arr[i] == 0:
                arr.insert(i,0)
                i+=2
                count+=1
            else:
                i+=1
        for _ in range (count):
            arr.pop()

        