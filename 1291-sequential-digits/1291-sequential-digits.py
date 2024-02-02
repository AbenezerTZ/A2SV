class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """      
        ans = []
        l = len(str(low))
        h = len(str(high))
        while l < h:
            num = [i for i in range(1,l+1)]
            while num[-1] < 9:
                if int("".join(map(str, num))) >= low:
                    ans.append(int("".join(map(str, num))))
                for i in range(len(num)):
                    num[i] += 1
            if int("".join(map(str, num))) >= low:
                ans.append(int("".join(map(str, num))))
            l += 1
        num = [i for i in range(1,l+1)]
        while num[-1] <= 9 and (int("".join(map(str, num)))) <= high:
            if int("".join(map(str, num))) >= low:
                ans.append(int("".join(map(str, num))))
            for i in range(len(num)):
                num[i] += 1
        return ans
         
            
            
        