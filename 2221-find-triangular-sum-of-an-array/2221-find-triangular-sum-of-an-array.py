class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def result(num):
            if len(num)==1:
                return num[0]
            temp = []
            for i in range(len(num)-1):
                if num[i] + num[i+1] >= 10:
                    temp.append((num[i] + num[i+1])-10)
                else:
                    temp.append(num[i] + num[i+1])
            return result(temp)
        return result(nums)
        
            
        