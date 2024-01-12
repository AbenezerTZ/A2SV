class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        k = 0
        
        s = sorted(arr)
        if s==arr:
            return ans
        
        while arr != s:
            maxi = max(0,len(arr)-k)
            if arr[0]==maxi:
                arr[:len(arr)-k] = arr[:len(arr)-k][::-1]
                ans.append(len(arr)-k)
                k += 1
            else:
                for i in range(1,len(arr)-k):
                    if arr[i]==maxi:
                        arr[:i+1] = arr[:i+1][::-1]
                        ans.append(i+1)
        return ans