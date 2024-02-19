class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        ans = []
        for i in range(len(l)):
            temp = [nums[j] for j in range(l[i], r[i]+1)]
            flag = True
            temp.sort()
            x = temp[1] - temp[0]
            for n in range(1,len(temp)-1):
                if temp[n+1] - temp[n] != x:
                    ans.append(False)
                    flag = False
                    break
                    
            if flag:
                ans.append(True)
        return ans
                
        