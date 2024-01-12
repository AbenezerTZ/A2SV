class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        res = []
        num = str(num)
        for i in range(len(num)):
            res.append(num[i])
        if res[0]=="-":
            res.sort(reverse=True)
            res.remove(res[-1])
            return int("-"+ "".join(res))
        else:
            ans = []
            res.sort()
            for i in res:
                if i == "0":
                    count += 1
                else:
                    ans.append(i)
            if len(ans) > 2:
                ans[0] += "0"*count
            elif len(ans) == 2:
                ans[-2] += "0"*count
            else:
                ans.append("0"*count)
            return int("".join(ans))
                    
                    
            
        