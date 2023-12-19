class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        x = False
        for i in range(len(num)):
            if int(num[i])%2!=0:
                x = True
                temp = num[:i+1]
        if x:
            return str(temp)
        else:
            return ""
        