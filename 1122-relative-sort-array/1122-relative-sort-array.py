class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        freq = {}
        ans = []
        for i in arr1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i in arr2:
            for _ in range(freq[i]):
                ans.append(i)
        if len(ans)==len(arr1):
            return ans
        temp = []
        for i in arr1:
            if i not in arr2:
                temp.append(i)
        temp.sort()
        ans.extend(temp)
        arr1 = ans
        return arr1
        
        