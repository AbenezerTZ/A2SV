class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        count = 0
        ave = sum(arr[:k])
        if ave//k >= threshold:
            count += 1
        for i in range(1,len(arr)-k+1):
            ave -= arr[i-1]
            ave += arr[i+k-1]
            if ave//k >= threshold:
                count += 1
        return count